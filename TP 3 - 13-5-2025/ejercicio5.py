import os
os.system("cls")

numero = int(input("Ingresa un número: "))

es_primo = True

if numero < 2:
    es_primo = False
else:
    for a in range(2, int(numero ** 0.5) + 1):
        if numero % a == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")