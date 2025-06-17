# Complementario 1
v1 = [int(input()) for _ in range(3)]
v2 = [int(input()) for _ in range(3)]
escalar = sum(v1[i]*v2[i] for i in range(3))
print("Producto escalar:", escalar)
x = v1[1]*v2[2] - v1[2]*v2[1]
y = -(v1[0]*v2[2] - v1[2]*v2[0])
z = v1[0]*v2[1] - v1[1]*v2[0]
print("Producto vectorial:", x, "i", y, "j", z, "k")

# Complementario 2
n = int(input())
v = [input() for _ in range(n)]
for i in range(n // 2):
    v[i], v[n - 1 - i] = v[n - 1 - i], v[i]
print(v)

# Complementario 3
primos = [True] * 100
primos[0] = False
for i in range(1, 99):
    if primos[i]:
        for j in range(i+1, 100):
            if (j+1) % (i+1) == 0:
                primos[j] = False
for i in range(100):
    if primos[i]:
        print(i+1)

# Complementario 4
v = []
n = int(input())
while True:
    o = int(input())
    if o == 0:
        break
    if o == 1 and len(v) < n:
        v.append(int(input()))
    elif o == 2 and v:
        x = int(input())
        if x in v:
            v.remove(x)
    elif o == 3:
        print(v)
    elif o == 4:
        x = int(input())
        print(v.count(x))
    elif o == 5:
        print("Media:", sum(v)/len(v), "Máximo:", max(v))

# Complementario 5
v = [int(input()) for _ in range(int(input()))]
x = int(input())
if x in v:
    print(v.index(x)+1)

# Complementario 6
v = [int(input()) for _ in range(int(input()))]
v.sort(reverse=True)
print(v)

# Complementario 7
v = [int(input()) for _ in range(10)]
v.append(int(input()))
v.sort()
print(v)

# Complementario 8
v = [int(input()) for _ in range(int(input()))]
pares = [x for x in v if x % 2 == 0]
impares = [x for x in v if x % 2 != 0]
print("Pares:", pares)
print("Impares:", impares)
if len(pares) > len(impares):
    print("Más pares")
elif len(impares) > len(pares):
    print("Más impares")
else:
    print("Iguales")

# Complementario 9
v = [input() for _ in range(int(input()))]
x = input()
for i in range(len(v)):
    if v[i] == x:
        if i > 0:
            print(v[i-1])
        if i < len(v)-1:
            print(v[i+1])
