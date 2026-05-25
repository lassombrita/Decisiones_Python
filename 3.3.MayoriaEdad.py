# 3.3.MayoriaEdad - Determina si una persona es mayor o menor de edad

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    mensajeEdad = "Mayor de edad"
else:
    mensajeEdad = "Menor de edad"

print("Hola", nombre)
print("usted es", mensajeEdad)
