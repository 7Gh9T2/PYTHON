#cargar e imprimir una lista con funciones
#definimos una lista vacia
lista = []

#definimos la funcion que permitirá cargar la lista

def cargar_lista(dato):
    lista.append(dato)

#recibir una cantidad indeterminada de argumentos
def cargar_lista(*args):
    for arg in args:
        lista.append(arg)

def imprimir_lista():
    for item in lista:
        print(item, end=' | ')

#ejecutamos las funciones
cargar_lista(25)
cargar_lista(50)
cargar_lista(75)
cargar_lista(100)

#imprimimos la lista
imprimir_lista()

cargar_lista('A','B','C',[125,852,963])

imprimir_lista()