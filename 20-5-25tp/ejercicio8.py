import os
os.system("cls")

PI = 3.1416

print("Ingrese valores del menu: ")
print("1 - Area del triangulo: ")
print("2 - Area del circulo: ")

Opc = int(input("Opc: "))

if Opc == 1:
    print("Area del triangulo")
    print("Ingrese el lado del triangulo")
    L = float(input("L: "))
    A = ((3 ** 0.5)/4) * L**2
    print("\nEl area del triangulo es:", A)

elif Opc == 2:
    print("Area del circulo")
    print("Ingrese el radio del circulo")
    R = float(input("R: "))
    C = PI * R**2
    print("\nEl area del circulo es:", C)

else:
    print("\nError")