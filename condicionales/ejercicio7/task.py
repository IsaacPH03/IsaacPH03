puntuacion = float(input("Introduce tu puntuación:"))
monto = 2400 * puntuacion
Inaceptable = 0.0
Aceptable = 0.4
Meritorio = 0.6
if puntuacion == Meritorio:
    print("tu nivel de rendimiento es", Meritorio)
elif puntuacion == Inaceptable:
    print("tu nivel de rendimiento es", Inaceptable)
elif puntuacion == Aceptable:
    print("tu nivel de rendimiento es", Aceptable)
else:
    print("Esta puntuación no es válida")
