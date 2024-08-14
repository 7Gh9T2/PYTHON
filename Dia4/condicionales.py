# Solicitar los números al usuario
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

# Determinar el número mayor
if numero_1 > numero_2:
    mayor = numero_1
elif numero_2 > numero_1:
    mayor = numero_2
else:
    mayor = numero_1  # Si son iguales, elige cualquiera de los dos

# Imprimir el número mayor
print(f"El número mayor es: {mayor}")

# Verificar si el número mayor es par o impar
if mayor % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

else:
  print("Los numeros ingesados son iguales")

print("---------------------------------------------------------")
usuario = input ("Ingrese su usuario")
password= input("Ingrese su contraseña: ")
if(usuario == "admin" and password)  