
import numpy as np
import pandas as pd

X=np.genfromtxt("matrix.txt")
print(X)

matriz = np.matrix(np.genfromtxt("matrix.txt"))
vector = np.matrix(np.genfromtxt("matrix.txt"))

U = np.shape(matriz)
V = matriz.size

A = np.shape(vector)
B = vector.size

m = U[0]

x = np.zeros((m))

for i in range(0,U[0]):
    for j in range(0, U[0]-1):
        factor = ((matriz[i,j])/(matriz[i,j]))
        for c in range(0, U[0]):
            matriz[i,j] = matriz[i,j] - (factor*matriz[i,j])
            print(matriz)

for i in range(0,U[0]):
    for j in range(0, U[0]-1):
        factor = ((matriz[i][j])/(matriz[i][j]))
        for c in range(0, U[0]):
            matriz[i][j] = matriz[i][j] - (factor*matriz[i][j])
            print(matriz)

for n in range(0, A[0]):
    for m in range(A[0]-1, U[0]):
        factor = ((matriz[n,m])/(matriz[n,m]))
        vector[n,m] = vector[n,m] - (factor*vector[n,m])
        print(vector)


"""for k in range(0, m):
    for r in range(k+1, m):
        factor = (matriz[r, k]/matriz[k,k])
        vector[r] = vector[r] - (factor*vector[k])
        for c in range(0, m):
            matriz[r,c] = matriz[r,c] - (factor*matriz[k,c])
    print(matriz)"""
    

#sustitución hacia atrás
x[m-1] = vector[m-1]/matriz[m-1,m-1]
print(x[M-1])

for r in range(U[0]-2, -1, -1):
    suma = 0
    for c in range(0, n):
        suma = suma*matriz[r,c]*x[c]
        x[r] = (vector[r] - suma)/(matriz[r,r])
    #print(x[r])

print("resultado matriz")
print(matriz)
print("resultado vector")
print(vector)
