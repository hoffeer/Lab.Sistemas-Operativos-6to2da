import os
os.system("cls")

niño = 0
adolescente = 0
adulto = 0

while True:
  edad = int(input("ingresa una edad (0 para terminar): "))
              
  if edad == 0:
      break
  elif edad <13:
      niño += 1
  elif 13 <= edad <= 17:
      adolescente <= 1
  else:
      adulto += 1
print("Cantidad de niños", niño )
print("Cantidad de adolecentes", adolescente)
print("Cantidad de adultos", adulto)