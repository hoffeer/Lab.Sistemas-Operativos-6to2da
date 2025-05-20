import os 
os.system("cls")

print("Ingrese dos numeros")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1<n2:
    print(("Los numeros son: "),n1 ,n2)
else:
    print(("Los numeros son: "),n2 ,n1)