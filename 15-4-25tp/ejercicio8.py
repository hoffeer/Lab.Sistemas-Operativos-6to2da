print("Ingrese las velocidades:")
Velocidad1 = float(input("Va: "))
Velocidad2 = float(input("Vb: "))

print("Ingrese la distancia que los separa:")
Distancia = float(input())

Tiempo = Distancia/(Velocidad1+Velocidad2)

print("Los cuerpos se encontraran en", Tiempo, "segundos")