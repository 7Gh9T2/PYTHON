notas = []

# Leer datos
for x in range(3):
    nota = float(input(f"Ingrese la nota {x + 1}: ")) 
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Verificar si está aprobado o reprobado
if promedio > 1.7:
    print(f"Promedio: {promedio:.2f} - Aprobado")
else:
    print(f"Promedio: {promedio:.2f} - Reprobado")
