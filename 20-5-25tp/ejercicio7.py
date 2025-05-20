import os
os.system("cls")

print("Ingrese valores de la ecuacion cuadratica: ")

a=int(input("Valor 1: "))
b=int(input("Valor 2: "))
c=int(input("Valor 3: "))

d = b**2 - 4*a*c

if d<0:
    x1 = ((-b) + d**0.5)/2*a
    x2 = ((-b) + d**0.5)/2*a
    print("Raices Reales", x1,x2)
else:
    print("Raices Irracionales")