import os
os.system("cls")

print("Ingrese 5 notas de alumnos: ")
nota1 = int(input("Ingrese la nota: "))
nota2 = int(input("Ingrese la nota: "))
nota3 = int(input("Ingrese la nota: "))
nota4 = int(input("Ingrese la nota: "))
nota5 = int(input("Ingrese la nota: "))

promedio = nota1+nota2+nota3+nota4+nota5*5

if promedio >= 7:
    print("El promedio supera el 7")
else:
    print("El promedio no supera el 7")