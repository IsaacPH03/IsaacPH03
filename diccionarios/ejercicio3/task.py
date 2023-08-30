frutas = {'Plátano':50, 'Manzana':60, 'Pera':70,'Naranja':80}
pregunta=input("¿Qué fruta quieres?")
pregunta2=float(input("¿Cuántos kilos?"))
if pregunta in frutas:
    print(f"{frutas[pregunta]} kilos de Manzana valen {pregunta2*frutas[pregunta]}")
else:
    print(f"Lo siento, la fruta {pregunta} no está disponible.")

