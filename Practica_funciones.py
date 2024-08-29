#Crear una funcion que reciba una lista y otro argumento ASC o DESC, y ordene la lista de forma ascendente o descendente
#según el argumento recibido.

def ordenar_lista(lista, orden):
    if orden == 'ASC':
        lista.sort()
    elif orden == 'DESC':
        lista.sort(reverse=True)


mi_lista = [5, 3, 8, 2, 9]
ordenar_lista(mi_lista, 'ASC')
print(mi_lista) 

ordenar_lista(mi_lista, 'DESC')
print(mi_lista) 
