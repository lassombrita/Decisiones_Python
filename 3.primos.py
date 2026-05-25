# 3.primos - Determina si un número es primo

n = int(input("Ingrese un número: "))
contador = 0
for i in range(1, n + 1):
    if n % i == 0:
        contador += 1

if contador == 2:
    print(n, "es primo")
else:
    print(n, "no es primo")
