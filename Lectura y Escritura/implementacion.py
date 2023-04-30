import requests
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"id": "matrix"})

numRows = len(table.find_all("tr"))
numCols = len(table.find_all("tr")[0].find_all("td"))

matrix = []
for row in table.find_all("tr"):
  matrixRow = []
  for cell in row.find_all("td"):
    matrixRow.append(int(cell.text))
  matrix.append(matrixRow)

print(matrix)
print("Filas:", numRows)
print("Columnas:", numCols)
