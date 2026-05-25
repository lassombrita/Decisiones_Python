# 3.13.DescuentoArticulo - Aplica un descuento porcentual a un artículo

precio = float(input("Ingrese el precio del artículo: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
total = precio - (precio * descuento / 100)
print("El precio final con descuento es:", total)
