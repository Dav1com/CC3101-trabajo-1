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
    numVars = 0
    for i in formula:
        for j in i:
            if not (abs(j) in compresion):
                compresion[abs(j)] = k
                k += 1
            numVars = max(numVars, abs(j))
    return compresion, numVars

def genValuacion(compresion, numVars, evaluacion):
    arr = [None] * numVars
    for i in range(numVars):
        if i+1 in compresion:
            arr[i] = not not((evaluacion >> compresion[i+1]) & 1)
        else:
            arr[i] = False
    return arr

def comprobarSatisfacible(formula):
    compresion, numVars = comprimirVariables(formula)
    for evaluacion in range(2**(len(compresion) + 1)):
        resultado = True
        for clausura in formula:
            resultadoClausura = False
            for literal in clausura:
                if literal > 0:
                    evalLiteral = (evaluacion >> compresion[literal]) & 1
                    resultadoClausura = resultadoClausura or evalLiteral
            resultado = resultado and resultadoClausura
        if resultado:
            return True, genValuacion(compresion, numVars, evaluacion)
    return False, None

def parte3(x, n_max, rep):
    for k in range(3, x+1):
        for n in range(1, n_max): # O(x*n)
            satisfactibles = 0
            for i in range(rep):  # O(rep*x*n*2^x)
                formula = generar3CNF(k, n)
                satisfacible, evalu = comprobarSatisfacible(formula) # O(2^x)
                satisfactibles += satisfacible
            print(", ".join([str(k), str(n), str(satisfactibles), str(rep-satisfactibles)]))

def main():
    parte3(15, 100, 1000)
    return 0

if __name__ == "__main__":
    main()
