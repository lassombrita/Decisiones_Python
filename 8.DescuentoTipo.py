# 8.DescuentoTipo - Aplica descuento según tipo de cliente (VIP/Normal)

precio = float(input("Ingrese el precio del artículo: "))
tipo = input("Ingrese el tipo de cliente (VIP/Normal): ")

if tipo == "VIP":
    precio = precio * 0.80  # 20% descuento
else:
    precio = precio * 0.95  # 5% descuento

print("El precio final es:", precio)
