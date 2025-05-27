import os
os.system("cls")

edad = int(input("Ingrese su edad: "))

if edad <= 18:
    print("Usted es menor de edad")
elif edad >= 18 and edad <= 64:
    print("Usted es adulto")
else:
    print("Usted es adulto mayor")