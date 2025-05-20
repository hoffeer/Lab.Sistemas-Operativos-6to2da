import os
os.system("cls")

print("Ingrese la velocidad de ambos vehiculos: ")

v1 = int(input("Velocidad 1: "))
v2 = int(input("Velocidad 2: "))

print("Ingrese la distancia que los separa: ")
d = int(input("Distancia: "))

if v1>0 and v2>0:
    t = d/(v1+v2)
    print(t,"segundos")
else:
    print("HUBO UN ERROR")