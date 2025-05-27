import os 
os.system("cls")

semana = int(input("Ingresar un número del 1 al 7 representando un día de la semana (1: lunes, 7: domingo)"))

if semana <= 5:
    print("El dia ingresado es un dia laboral")
elif semana >= 6 and semana <= 7:
    print("El dia ingresado es un dia de fin de semana")
else:
    print("El numero ingresado no es un dia")