import os 
os.system("cls")

monto = 100000

retiro = int(input("Ingrese un monto a retirar: "))

if retiro <= monto:
    saldorestante = monto - retiro
    print("La operacion fue realizada con exito. Su saldo restante es", saldorestante)
else:
    print("Fondos Insuficientes")