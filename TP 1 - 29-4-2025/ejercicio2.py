import os
os.system("cls")

velocidad = int(input("Ingrese la velocidad de su vehiculo: "))

if velocidad <= 60:
    print("Está dentro del límite permitido")
elif velocidad > 60 and velocidad <= 80:
    print("Esta en exceso leve")
else:
    print("Esta en exceso grave")