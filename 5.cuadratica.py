# 5.cuadratica - Resuelve la ecuación cuadrática ax² + bx + c = 0

import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d = b**2 - 4*a*c
if d < 0:
    print("La ecuación no tiene soluciones reales")
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Las soluciones son:", x1, "y", x2)
