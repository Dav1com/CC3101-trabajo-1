from pysat.formula import CNF
from pysat.solvers import Minisat22
from stopwatch import StopWatch
from typing import Tuple, Callable


def comprobar_satisfacible_minisat(formula : list) -> Tuple[bool, list]:
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


#assert comprobar_satisfacible_minisat([[1, -3, 5], [-2, 5, -4], [3, -1, 2], [-5, -3, 2]]) == (True, [-1, -2, -3, -4, -5])