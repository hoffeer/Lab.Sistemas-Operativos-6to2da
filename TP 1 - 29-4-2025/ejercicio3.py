import os 
os.system("cls")

print("MENU")
print("1- Hamburguesa")
print("2- Pizza")
print("3- Ensalada")
print("")
print("Pulse 4 para Salir")

while True:
    opc=int(input("Ingrese lo que desea:"))
    if opc == 1:
        print("Usted ordeno una hamburguesa")
    elif opc== 2:
        print("usted ordeno una pizza")
    elif opc == 3:
        print("Usted ordeno una ensalada")
    else:
        break