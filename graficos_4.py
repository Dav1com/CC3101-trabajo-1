import matplotlib.pyplot as plt
import numpy


MIN_K = 0
MAX_K = 12
DEBUG = True



c1 = []
c2 = []

f = open('out-parte-4.txt', 'r')

for line in f:
    a, b = (float(x) for x in line.split(" "))
    c1.append(a)
    c2.append(b)

f.close()

eje_x = numpy.arange(3, len(c1) + 3, 1)
plt.plot(eje_x, c1, label="Fuerza bruta")
plt.legend()
plt.plot(eje_x, c2, label="Minisat22")  # todo: hacer mas modular esto
plt.legend()
plt.title("Tiempo de ejecución vs número de \n variables para distintos algoritmos.")
plt.ylabel("Tiempo de ejecución. (segundos)")
plt.xlabel("Número de variables.")

plt.yscale("log")
plt.show()



