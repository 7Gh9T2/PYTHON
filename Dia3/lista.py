calificaciones = [1,2,3,4,5]
nombres = ["Moises","Camila","Fernanda","Pablo","tania"]
lista_variada = [True, 10.5,"abc",[0,1,1]]

print("Estudiante: ",nombres[2])
print("Calificacion: ", calificaciones[-2])
print("Lista dentro de otra ", lista_variada[3][0])
print("Imprimir un rango o cicles ",nombres[1:2])
print(lista_variada)

nombres.append("Anibal")
print(nombres)

nombres.remove("Pablo")
print(nombres)