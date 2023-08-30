asignatura = {}

asignatura.update({"Matemáticas":int(input("Ingrese el valor del crédito para Matemáticas"))})
asignatura.update({"Física":int(input("Ingrese el valor del crédito para Física"))})
asignatura.update({"Química":int(input("Ingrese el valor del crédito para Química"))})

print('Matemáticas','tiene', asignatura['Matemáticas'],'créditos')
print('Física','tiene', asignatura['Física'],'créditos')
print('Química','tiene', asignatura['Química'],'créditos')
print("Número total de créditos del curso:", sum(asignatura.values()))