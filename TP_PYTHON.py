# Ejercicio 1: Cálculo de distancia
V = float(input("Velocidad (m/s): "))
T = int(input("Tiempo (s): "))
D = V * T
print("El móvil se movilizó por", D, "metros.")

# Ejercicio 2: Promedio de notas
N1 = float(input("Ingrese su primera nota: "))
N2 = float(input("Ingrese su segunda nota: "))
N3 = float(input("Ingrese su tercera nota: "))
NF = (N1 + N2 + N3) / 3
print("El promedio final es", NF)

# Ejercicio 3: Puntaje de respuestas
RC = int(input("Respuestas correctas: "))
RI = int(input("Respuestas incorrectas: "))
RB = int(input("Respuestas en blanco: "))

PRC = RC * 3
PRI = RI * -1
PRB = RB * 0
PF = PRC + PRI + PRB
print("El puntaje final es de", PF)

# Ejercicio 4: Puntaje en partidos
PG = int(input("Partidos ganados: "))
PP = int(input("Partidos perdidos: "))
PE = int(input("Partidos empatados: "))

PGT = PG * 3
PPT = PP * 0  
PET = PE * 1  
PF = PGT + PPT + PET
print("El puntaje final es de", PF)

# Ejercicio 5: Cantidad de discos necesarios
T = float(input("Ingrese el tamaño de la copia (GB): "))
MD = 1.44  
GB = 1024  
DR = (GB * T) / MD
print("Se requieren", round(DR), "discos.")

# Ejercicio 6: Distancia entre dos puntos
AX = float(input("Ingrese el valor de x de A: "))
AY = float(input("Ingrese el valor de y de A: "))
BX = float(input("Ingrese el valor de x de B: "))
BY = float(input("Ingrese el valor de y de B: "))

D = ((AY - BY) * 2 + (AX - BX) * 2) ** 0.5
print("La distancia entre A y B es de:", D, "m.")

# Ejercicio 7: Área de un triángulo
N1 = float(input("Primer número: "))
N2 = float(input("Segundo número: "))
P = (N1 * N2) / 2
print("El área del triángulo es:", P)

# Ejercicio 8: Perímetro y área de un rectángulo
a = float(input("Altura: "))
b = float(input("Base: "))
p = 2 * (a + b)
ar = a * b
print("El perímetro es de", p, "y el área es de", ar)

# Ejercicio 9: Costo de combustible
a = float(input("Ingresar el consumo en galones: "))
g = 3.785  
p = 4.50 
pt = a * g * p
print("El precio total es de", pt)

# Ejercicio 10: Volumen y área de un cilindro
o = float(input("Ingresa el radio: "))
a = float(input("Ingresa el alto: "))
pi = 3.1416

V = pi * (o ** 2) * a
SON = 2 * pi * o * a

print("El volumen es de:", V)
# Ejercicio 1: Cálculo de distancia
V = float(input("Velocidad (m/s): "))
T = int(input("Tiempo (s): "))
D = V * T
print("El móvil se movilizó por", D, "metros.")

# Ejercicio 2: Promedio de notas
N1 = float(input("Ingrese su primera nota: "))
N2 = float(input("Ingrese su segunda nota: "))
N3 = float(input("Ingrese su tercera nota: "))
NF = (N1 + N2 + N3) / 3
print("El promedio final es", NF)

# Ejercicio 3: Puntaje de respuestas
RC = int(input("Respuestas correctas: "))
RI = int(input("Respuestas incorrectas: "))
RB = int(input("Respuestas en blanco: "))

PRC = RC * 3
PRI = RI * -1
PRB = RB * 0
PF = PRC + PRI + PRB
print("El puntaje final es de", PF)

# Ejercicio 4: Puntaje en partidos
PG = int(input("Partidos ganados: "))
PP = int(input("Partidos perdidos: "))
PE = int(input("Partidos empatados: "))

PGT = PG * 3
PPT = PP * 0  
PET = PE * 1  
PF = PGT + PPT + PET
print("El puntaje final es de", PF)

# Ejercicio 5: Cantidad de discos necesarios
T = float(input("Ingrese el tamaño de la copia (GB): "))
MD = 1.44  
GB = 1024  
DR = (GB * T) / MD
print("Se requieren", round(DR), "discos.")

# Ejercicio 6: Distancia entre dos puntos
AX = float(input("Ingrese el valor de x de A: "))
AY = float(input("Ingrese el valor de y de A: "))
BX = float(input("Ingrese el valor de x de B: "))
BY = float(input("Ingrese el valor de y de B: "))

D = ((AY - BY) * 2 + (AX - BX) * 2) ** 0.5
print("La distancia entre A y B es de:", D, "m.")

# Ejercicio 7: Área de un triángulo
N1 = float(input("Primer número: "))
N2 = float(input("Segundo número: "))
P = (N1 * N2) / 2
print("El área del triángulo es:", P)

# Ejercicio 8: Perímetro y área de un rectángulo
a = float(input("Altura: "))
b = float(input("Base: "))
p = 2 * (a + b)
ar = a * b
print("El perímetro es de", p, "y el área es de", ar)

# Ejercicio 9: Costo de combustible
a = float(input("Ingresar el consumo en galones: "))
g = 3.785  
p = 4.50 
pt = a * g * p
print("El precio total es de", pt)

# Ejercicio 10: Volumen y área de un cilindro
o = float(input("Ingresa el radio: "))
a = float(input("Ingresa el alto: "))
pi = 3.1416

V = pi * (o ** 2) * a
SON = 2 * pi * o * a

print("El volumen es de:", V)
print("El área es de:", SON)