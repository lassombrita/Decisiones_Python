# 3.15.aspiranteEjercito - Verifica si cumple requisitos para el ejército

edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ")

if 18 <= edad <= 25:
    if genero == "M":
        print("Cumple requisitos para aspirar al ejército")
    else:
        print("No cumple requisitos por género")
else:
    print("No cumple requisitos por edad")
