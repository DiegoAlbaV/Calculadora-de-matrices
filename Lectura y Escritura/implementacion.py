from bs4 import BeautifulSoup
import requests

with open("index.html") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table", {"id": "tblmatrices"})

rows = table.find_all("tr")
num_rows = len(rows)
num_cols = len(rows[0].find_all("td"))

matriz = []
for row in rows:
    fila = []
    for cell in row.find_all("td"):
        valor = cell.find("input").get("value")
        if valor:
            try:
                valor = int(valor)
                fila.append(valor)
            except ValueError:
                print("Error: Ingrese un valor numérico")
                exit()
    if len(fila) != num_cols:
        print("Error: La matriz debe tener todas sus filas con la misma cantidad de elementos")
        exit()
    matriz.append(fila)

print("Matriz: ", matriz)
print("Número de filas: ", num_rows)
print("Número de columnas: ", num_cols)

matriz_resultante = matriz
num_filas_resultante = num_rows
num_columnas_resultante = num_cols
