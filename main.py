from random import randint
from random import sample
from math import floor

def generar3CNF(n, k):
    '''
    n es la cantidad de clausulas
    k es la cantidad de variables propocicionales (k >= 3)
    '''
    arr = []
    variables = range(1, k+1)
    for i in range(n):
        arr2 = [ (randint(0,1)*2 - 1) * i for i in sample(variables, 3) ]
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
                evalLiteral = (evaluacion >> compresion[abs(literal)]) & 1
                resultadoClausura = resultadoClausura or (evalLiteral if literal > 0 else not evalLiteral)
            resultado = resultado and resultadoClausura
        if resultado:
            return True, genValuacion(compresion, numVars, evaluacion)
    return False, None

def parte3(x, n_max, rep):
    for k in range(3, x+1):
        for n in range(1, n_max+1): # O(x*n)
            satisfactibles = 0
            for i in range(rep):  # O(rep*x*n*2^x)
                formula = generar3CNF(n, k)
                satisfacible, evalu = comprobarSatisfacible(formula) # O(2^x)
                satisfactibles += satisfacible
            print(", ".join([str(k), str(n), str(satisfactibles), str(rep - satisfactibles)]))

def main():
    parte3(12, 60, 1000)
    return 0

if __name__ == "__main__":
    main()
