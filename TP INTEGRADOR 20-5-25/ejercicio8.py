minutos = []
print("Ingrese los minutos de ejercicio diario (7 días):")
for i in range(7):
    m = int(input(f"Día {i+1}: "))
    minutos.append(m)

prom = sum(minutos) / 7
print("Promedio diario de ejercicio:", prom)
if prom < 30:
    print("Recomendación: aumentar la actividad física.")