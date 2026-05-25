# 3.4.MayorNumero - Encuentra el mayor entre dos números

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 > n2:
    mayor = n1
else:
    mayor = n2

print("El mayor entre", n1, "y", n2)
print("es", mayor)
