import os
os.system("cls")

costo = int(input("Ingrese el valor del articulo: "))

marca = input("Ingrese la marca: ")

if costo >= 2000 and marca == "NOSY":
    pa = costo*0.90
    pt = pa*0.95

elif costo >= 200 and marca != "NOSY":
    pt = costo*0.90

elif costo < 2000 and marca == "NOSY":
    pa = costo*0.95
    pt = pa + pa*0.20

elif costo < 2000 and marca != "NOSY":
    pa = costo*1.20

print("Debe de pagar: "), pt, "soles"