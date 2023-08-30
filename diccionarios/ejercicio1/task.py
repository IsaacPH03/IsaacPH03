moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa:")
if divisa in moneda:
    print(moneda.get(divisa))
else:
    print("La divisa no está.")