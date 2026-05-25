# 2.tanqueAgua - Calcula cuántos días dura el agua de un tanque

capacidad = float(input("Ingrese la capacidad del tanque en litros: "))
consumo = float(input("Ingrese el consumo diario en litros: "))
dias = capacidad / consumo
print("El agua del tanque durará", dias, "días")
