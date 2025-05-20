import os
os.system("cls")

print("Ingrese los 3 numeros: ")

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))

if a<0:
    r = a*b*c
else:
    r = a+b+c

print(r)