# 3.9.MensajeNota - Clasifica una nota en categorías

nota = float(input("Ingrese su nota definitiva: "))
print("Su nota es:", nota)

if nota < 3.0:
    print("Nota insuficiente")
elif nota < 3.5:
    print("Aceptable")
elif nota < 4.0:
    print("Sobre saliente")
else:
    print("Excelente")
