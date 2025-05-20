import os
os.system("cls")

print = ("Ingrese la fecha: ")

año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

if dia>0 and dia<30:
    print("Mañana es:", dia+1, mes,año)
else:
    if mes > 0 and mes < 12:
        print("Mañana es:", 1, mes+1, año)
    else:
        print("Mañana es:", 1, 1,año+1)