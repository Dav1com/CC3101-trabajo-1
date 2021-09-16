from typing import Callable, List, Tuple
import matplotlib.pyplot as plt
from pregunta_4 import prueba_tiempo
import numpy


MIN_K = 0
MAX_K = 12
DEBUG = True



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

            if variables != n_previo: # Nuevo run de numeros de varaible
                if len(temp_lista) > 0:
                    optimas.append( min(temp_lista, key=lambda p: p[2])[:2])
                temp_lista = []
                n_previo = variables

            diferencia = abs(insatisfacibles - satisfacibles)
            temp_lista.append((variables, clausulas, diferencia))
        else:
            optimas.append(min(temp_lista, key=lambda p: p[2])[:2])

    return optimas # Variable, Clausula


print(encontrar_tuplas_optimas("out.txt"))

def grafico_comprobadores(casos: int, archivo: str, generador: Callable, comprobador1: Callable, comprobador2: Callable) -> None:
    """
    Genera un grafico comparando dos comprobadores de satisfacibilidad.
    @param casos: Numero de casos para probar para cada intervalo de k.
    @param archivo: archivo con los datos de numero de variables y clausulas.
    @param generador: Generador de CNFs.
    @param comprobador1: Primera funcion de satisfacibilidad.
    @param comprobador2: Segunda funcion de satisfacibilidad
    """

    # Ejemplo: grafico_comprobadores(100, "out.txt", generar3CNF, comprobarSatisfacible, comprobar_satisfacible_minisat)
    c1 = []
    c2 = []
    datos = encontrar_tuplas_optimas(archivo)

    for tupla in datos:
        k, n = tupla
        c1.append(prueba_tiempo(casos, n, k, generador, comprobador1))
        c2.append(prueba_tiempo(casos, n, k, generador, comprobador2))

    eje_x = numpy.arange(3, datos[len(datos) - 1][0] + 1, 1)
    plt.plot(eje_x, c1, label="Fuerza bruta")
    plt.legend()
    plt.plot(eje_x, c2, label="Minisat22")  # todo: hacer mas modular esto
    plt.legend()
    plt.title("Tiempo de ejecución vs número de \n variables para distintos algoritmos.")
    plt.ylabel("Tiempo de ejecución. (segundos)")
    plt.xlabel("Número de variables.")

    plt.yscale("log")
    plt.show()



