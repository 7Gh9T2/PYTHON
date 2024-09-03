#mostrar los numeros pares de 1 al 100
# Usando while y otro con for

x = 2
while x <= 100:
    print(x)
    x += 2  # Incrementa x en 2 para obtener solo los números pares

# Usando for
for x in range(2, 101, 2):  # Genera números pares del 2 al 100
    print(x)
