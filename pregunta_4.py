from pysat.formula import CNF
from pysat.solvers import Minisat22
from stopwatch import StopWatch
from typing import Tuple, Callable, List


def comprobar_satisfacible_minisat(formula: list) -> Tuple[bool, list]:
    """
    Comprueba si un arreglo en forma CNF es satisfacible
    Retorna una tupla de si es satisfacible (bool) y la valuacion testigo si es que existe.
    """

    _cnf = CNF(from_clauses=formula)
    with Minisat22(bootstrap_with=_cnf) as m:
        es_satisfacible = m.solve()
        valuacion_testigo = m.get_model()
    return es_satisfacible, valuacion_testigo


def prueba_tiempo(casos: int, n: int, k: int, generador: Callable, comprobador: Callable) -> float:
    """
    Testea la cantidad de tiempo que se demora un generador de CNFs en ser comprobadas como verificables.
    :param casos: Numero de casos por probar.
    :param n: Cantidad de clausulas para el generador.
    :param k: Cantidad de variables proporcionales. (k >= 3)
    :param generador: Funcion generadora de CNFs.
    :param comprobador: Funcion comprobadora de la satisfaciblidad de CNFs.
    :return: Float correspondiendo al tiempo transcurrido en segundos
    Ejemplo: prueba_tiempo(10000, 4, 5, generar3CNF, comprobar_satisfacible_minisat)
    """

    stopwatch = StopWatch()
    stopwatch.start()
    for i in range(casos):
        c = generador(n, k)
        comprobador(c)
    return stopwatch.stop()


def encontrar_tuplas_optimas(archivo: str) -> List[Tuple[int, int]]:
    """
    Funcion auxiliar para tomar un output del paso 3, y convertirlo en una lista de tuplas de
    numeros de clausulas y variables de razón optima.
    @param archivo: Path de un archivo de output
    @return: Lista de tuplas de la forma (Variables, Clausulas)
    """
    optimas = []

    # variable clausula satisfacible insatisfacible
    n_previo = -1
    temp_lista = []

    with open(archivo, "r") as file:
        for line in file:
            variables, clausulas, satisfacibles, insatisfacibles = [int(x) for x in line.split(', ')]

            if variables != n_previo:  # Nuevo run de numeros de varaible
                if len(temp_lista) > 0:
                    optimas.append(min(temp_lista, key=lambda p: p[2])[:2])
                temp_lista = []
                n_previo = variables

            diferencia = abs(insatisfacibles - satisfacibles)
            temp_lista.append((variables, clausulas, diferencia))
        else:
            optimas.append(min(temp_lista, key=lambda p: p[2])[:2])

    return optimas  # Variable, Clausula


def comparar_comprobadores(casos: int, archivo: str, generador: Callable, comprobador1: Callable, comprobador2: Callable) -> None:
    """
    Genera un archivo con los resultados de los testeos de tiepmo de dos distintos comprobadores.
    @param casos: Numero de veces para probar cada combinación de variables y clausulas.
    @param archivo: Archivo que contenga los pares de variables-clausulas
    @param generador: Generador de CNFs
    @param comprobador1: Funcion comprobadora 1
    @param comprobador2: Funcion comprobadora 2
    @return: None, pero crea un archivo 'out-parte-4.txt' con space separated values.
    """
    f = open('out-parte-4.txt', 'w')

    datos = encontrar_tuplas_optimas(archivo)

    for tupla in datos:
        k, n = tupla

        c1 = prueba_tiempo(casos, n, k, generador, comprobador1)
        c2 = prueba_tiempo(casos, n, k, generador, comprobador2)

        f.write(str(c1) + " " + str(c2) + "\n")

    f.close()
