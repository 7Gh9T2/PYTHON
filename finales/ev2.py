#leer por teclado dos numeros e imprimir el mayor o si ambos son iguales

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("Los números ingresados fueron: num1 =", num1, "y num2 =", num2)

# Comparar los números e imprimir el resultado
if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales.")
