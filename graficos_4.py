from typing import Callable
import matplotlib.pyplot as plt
from pregunta_4 import prueba_tiempo
import numpy


MIN_K = 3
MAX_K = 12
DEBUG = True


def grafico_comprobadores(casos: int, razon: float, generador: Callable, comprobador1: Callable, comprobador2: Callable) -> None:
    """
    Genera un grafico comparando dos comprobadores de satisfacibilidad.
    @param casos: Numero de casos para probar para cada intervalo de k.
    @param razon: Razon entre numero de variables y clausulas.
    @param generador: Generador de CNFs.
    @param comprobador1: Primera funcion de satisfacibilidad.
    @param comprobador2: Segunda funcion de satisfacibilidad
    """

    # Ejemplo: grafico_comprobadores(100, 5, generar3CNF, comprobarSatisfacible, comprobar_satisfacible_minisat)
    c1 = []
    c2 = []

    for k in range(MIN_K, MAX_K):
        n = int(k * razon)
        c1.append(prueba_tiempo(casos, n, k, generador, comprobador1))
        c2.append(prueba_tiempo(casos, n, k, generador, comprobador2))
        if DEBUG:
            print("k:", k)

    eje_x = numpy.arange(MIN_K, MAX_K, 1)
    plt.plot(eje_x, c1, label="Fuerza bruta")
    plt.legend()
    plt.plot(eje_x, c2, label="Minisat22")  # todo: hacer mas modular esto
    plt.legend()
    plt.title("Tiempo de ejecución vs número de \n variables para distintos algoritmos.")
    plt.ylabel("Tiempo de ejecución. (segundos)")
    plt.xlabel("Cantidad de variables. Clausulas en razón 1:" + str(razon) + ".")

    #plt.plot(eje_x, c2)
    plt.yscale("log")
    plt.show()


