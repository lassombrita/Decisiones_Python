# 3.8.SistemaOperativo - Detecta Android o iOS según letra ingresada

opcion = input("Ingrese un carácter: ")
print("Su opción es:")
if opcion == 'a' or opcion == 'A':
    print("Android")
elif opcion == 'i' or opcion == 'I':
    print("iOS")
else:
    print("Inválida")
