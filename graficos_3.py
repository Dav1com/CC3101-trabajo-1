import matplotlib.pyplot as plt
import numpy as np

f = open('out.txt', 'r')

Z = []

minX = int(1e18)
maxX = 0
minY = int(1e18)
maxY = 0
for line in f:
    line = line.split(', ')
    minX = min(minX, int(line[0]))
    maxX = max(maxX, int(line[0]))
    minY = min(minY, int(line[1]))
    maxY = max(maxY, int(line[1]))
    Z.append(abs(int(line[2]) - int(line[3])))

x = np.arange(minX - 0.5, maxX + 1, 1)
y = np.arange(minY - 0.5, maxY + 1, 1)
Z = np.array(Z).reshape(maxX-minX+1, maxY-minY+1).transpose()

plt.pcolormesh(x, y, Z)
plt.title("Diferencia absoluta entre formulas satisfacibles e insatisfacibles")
plt.xlabel("Cantidad de Variables")
plt.ylabel("Cantidad de Clausulas")
plt.colorbar(shrink = 0.85)
plt.show()

f.close()

