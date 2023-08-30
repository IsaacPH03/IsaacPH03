datos={}
datos.update({"nombre":input("¿Cómo te llamas?")})
datos.update({"Edad":input("¿Cuántos años tienes?")})
datos.update({"direccion":input("¿Cuál es tu dirección?")})
datos.update({"telefono":input("¿Cuál es tu número de teléfono?")})
print(f"{datos.get('nombre')} tiene {datos.get('Edad')} años, vive en {datos.get('direccion')} y su número de teléfono es {datos.get('telefono')}")