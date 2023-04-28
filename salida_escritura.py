import os

def escribirMatriz(matriz):
    contenido = "\n".join([" ".join(map(str, fila)) for fila in matriz])
    with open("salida.txt", "w") as archivo:
        archivo.write(contenido)
    os.startfile("salida.txt")
