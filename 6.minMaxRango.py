# 6.minMaxRango - Encuentra el mínimo y máximo entre tres números

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

menor = n1
mayor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3

print("El menor es:", menor)
print("El mayor es:", mayor)
