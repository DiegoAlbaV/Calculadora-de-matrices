import os
import sys
from string import Template

print("Programa que acepta datos de l estudiante y los muestra en una páguna web") ##era el ejemplo que saqué de innternet, pero basta con cambiar la entrada

filein = open('Template/plantilla.html') ##se abre la carpeta de HTML

src = Template(filein.read()) ##se abre la carpeta de HTML

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
matri = input("Digite su matrícula: ")

notas = []

while input("Quieres ingresar tus notas? Digite Si o No: ") == "si":
    if input == "no":
        continue
    nota = (int(input("ingresa la nota: ")))
    if nota <= 100 and nota >= 0:
        n = notas.append(nota)
    else:
        print("la nota no es valida")

        ##se guarda en diccionario los valores que queremos; con los nombres de variables que teníamos en plantilla.HTML
D = {'nombre':nombre, 'apellido':apellido, 'matri':matri, 'notas':notas, }

##se guarda el diccionario
result = src.substitute(D)

try:
    os.mkdir("perfil") ##se crea una carpeta con los valores de Result; 
    filein2 = open('perfil/'+'20175532'+'.html','a') ##se le asigna nombre al archivo con los valores de result
    filein2.writelines(result)  ##se camnbian los valores de las variables en las filas y columnas en plantilla.html
    print("Creando carpeta...")
    print("Guardando...")
except OSError:
    if os.path.exist('perfil'):
        filein2 = open('perfil/'+'20175532'+'.html','a')
        filein2.writelines(result)
        print("Guardando...")

while True:
    pregunta = input("dijite X si desea salir o Digite Y si desea agregar otro perfil: ")
    if pregunta == "y":
        os.system("Programa.py")
    elif pregunta == "x":
        sys.exit()
