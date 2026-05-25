# 3.12.SistemaOperativoSegun - Muestra el SO según opción (Segun → match/if-elif)

print("Seleccione su sistema operativo:")
print("1. Windows")
print("2. Linux")
print("3. MacOS")
print("4. Android")
opcion = int(input())

if opcion == 1:
    print("Sistema operativo Windows")
elif opcion == 2:
    print("Sistema operativo Linux")
elif opcion == 3:
    print("Sistema operativo MacOS")
elif opcion == 4:
    print("Sistema operativo Android")
else:
    print("Opción inválida")
