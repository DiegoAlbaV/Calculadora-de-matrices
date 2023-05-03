from tkinter import *
from tkinter import filedialog ##Crea un dialogo de archivos
#from algoritmo import gauss3
from fractions import Fraction
from tkinter import *

def crearMatriz():
    # obtener la matriz ingresada como una cadena
    matriz_str = entradaMatriz.get()

    # separar la cadena en una lista de filas
    filas_str = matriz_str.split(' ')

    # separar cada fila en una lista de valores
    matriz = []
    for fila_str in filas_str:
        valores_str = fila_str.split(',')
        valores = [float(valor) for valor in valores_str]
        matriz.append(valores)

    # procesar la matriz (por ejemplo, imprimir sus valores)
    print(matriz)

# crear la ventana principal
root = Tk()

# crear un campo de entrada de texto para la matriz
entradaMatriz = Entry(root)
entradaMatriz.grid(row=0, column=0)

# crear un botón para crear la matriz
Button(root, text="Crear matriz", command=crearMatriz).grid(row=1, column=0)

root.mainloop()