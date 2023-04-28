archivo = open("archivo.txt", "r") # abre el archivo en modo lectura

numeros = [] # lista para almacenar los números
num_filas = 0  # Contador de filas
num_cols = 0  # Contador de columnas

# Leemos el archivo línea por línea
for linea in archivo:
    num_filas += 1  # Incrementamos el contador de filas
    numeros_linea = []  # Lista para almacenar los números en la línea
    for caracter in linea:  # Iteramos sobre cada caracter de la línea
        if caracter.isdigit():  # Si el caracter es un número
            numeros.append(int(caracter))  # Lo agregamos a la lista como entero
            num = int(caracter)
            numeros_linea.append(num)  # Agregamos el número a la lista
    num_cols_linea = len(numeros_linea)  # Contamos el número de números en la línea
    if num_cols_linea > num_cols:  # Si encontramos más números que en cualquier otra línea anterior
        num_cols = num_cols_linea  # Actualizamos el contador de columnas



archivo.close() # cierra el archivo

#verifica qeu no sean ceros



#If para revisar los ceros
if all(numero == 0 for numero in numeros):
    print("Error: todos los números son cero")
else:       
#imprime la lista de números extraidos del texto
    print("Los números encontrados son:")
    print(numeros)
    print(f"El archivo tiene {num_filas} filas (m) y {num_cols} columnas (n).")
#x = numeros[0]
#y = numeros[1]
