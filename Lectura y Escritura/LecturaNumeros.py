archivo = open("archivo.txt", "r")
lineas = archivo.readlines()
archivo.close()

numeros_antes = []
numeros_despues = []
max_numeros_antes = 0
contador_m = 0

for linea in lineas:
    # Contar líneas
    contador_m += 1

    # Revisar si la línea contiene letras
    if any(c.isalpha() for c in linea):
        print("Matriz inválida")
        break

    # Buscar el índice del símbolo "=" en la línea
    index = linea.find("=")
    if index != -1:
        # Dividir la línea en dos partes por el signo "="
        parte1 = linea[:index].strip()
        parte2 = linea[index+1:].strip()

        # Leer los números de cada parte y detectar si deben ser negativos
        numeros1 = [int(x) if not (x.startswith('-') and x[1:].isdigit()) else -int(x[1:]) for x in parte1.split()]
        numeros2 = [int(x) if not (x.startswith('-') and x[1:].isdigit()) else -int(x[1:]) for x in parte2.split()]

        # Contar el número de números en la línea antes del signo "="
        num_numeros_antes = len(numeros1)
        if num_numeros_antes > max_numeros_antes:
            max_numeros_antes = num_numeros_antes

        # Agregar los números a los arreglos correspondientes
        numeros_antes.extend(numeros1)
        numeros_despues.extend(numeros2)

if numeros_antes and numeros_despues:
    print("Números antes del signo '=':", numeros_antes)
    print("Números después del signo '=':", numeros_despues)

print("m:", contador_m)
print("n:", max_numeros_antes)

# Crear matriz de m x n y llenarla con los datos del arreglo "numeros_antes"
matriz = []
for i in range(contador_m):
    fila = []
    for j in range(max_numeros_antes):
        index = i*max_numeros_antes + j
        if index < len(numeros_antes):
            fila.append(numeros_antes[index])
        else:
            fila.append(0)
    matriz.append(fila)

print("Matriz:")
for fila in matriz:
    print(fila)