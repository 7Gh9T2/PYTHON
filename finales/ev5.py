# Cargar una oración por teclado.
# Imprime la cantidad de vocales que tiene

cadena = input("Ingrese una oración: ")


vocales = 0


for caracter in cadena:
    
    if caracter in "aeiouAEIOU":
        vocales += 1


print("La oración ingresada es:", cadena)
print("La cantidad de vocales es:", vocales)
