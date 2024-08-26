diccionario = {
    "hola": "hello",
    "mundo": "world",  # Corregido "wordl" a "world"
    "perro": "dog",
    "gato": "cat"
}

while True:
    palabra = input("Introduce una palabra en español (o 0 para salir): ")

    if palabra == "0":
        break

    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es '{diccionario[palabra]}'.")
    else:
        print("La palabra no existe en el diccionario.")
        
        respuesta = input("¿Deseas agregar esta palabra al diccionario? (s/n): ")
        if respuesta.lower() == "s":
            traduccion = input(f"Introduce la traducción al diccionario de '{palabra}': ")
            diccionario[palabra] = traduccion
            print(f"'{palabra}' ha sido agregada al diccionario con la traducción '{traduccion}'.")

print("Traductor finalizado.")  # Esta línea ahora está fuera del bucle
