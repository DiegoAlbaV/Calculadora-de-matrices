 def leerMatriz():
    archivo = open("entrada.txt", "r")
    contenido = archivo.read()
    lineas = contenido.strip().split("\n")
    matriz = []
    
    for linea in lineas:
        valores = linea.strip().split(" ")
        matriz.append(list(map(int, valores)))
        
    # Procesa la matriz como desees
    resultado = [fila[::-1] for fila in matriz]
    
    # Escribe el resultado en un archivo de texto
    escribirMatriz(resultado)
    archivo.close()
