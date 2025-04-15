import math

PI = 3.1416

print("Ingrese lados del triangulo: ")
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("Ingrese el ángulo en grados sexagesimales: ")
alfa = float(input())

angulo = (b*2 + c*2 - 2*b*c * math.cos(alfa*PI/180))*0.50

print("El lado A es:", angulo)