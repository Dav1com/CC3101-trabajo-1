from random import randint
from math import floor

def generar3CNF(n, k):
    '''
    n es la cantidad de clausulas
    k es la cantidad de variables propocicionales (k >= 3)
    '''
    arr = []
    for i in range(n):
        arr2 = []
        for j in range(3): # [0, 3[
            arr2.append(randint(1, k) * (randint(0,1)*2 - 1))
        arr.append(arr2)
    return arr

def comprimirVariables(formula):
    compresion = {}
    k = 0
    for i in formula:
        for j in formula:
            if not (abs(j) in compresion):
                compresion[abs(j)] = k
                k += 1
    return compresion

def comprobarSatisfacible(formula):
    

def main():
    for i in range(10):
        print(generar3CNF(3, 5))
    return 0

if __name__ == "__main__":
    main()
