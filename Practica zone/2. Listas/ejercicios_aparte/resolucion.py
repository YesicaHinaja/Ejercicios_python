#1

lista_numeroes_enteros = [4,5,666,666,-2,4,3,8,100]

def calcular_promedio_enteros (list:list)->float:
    cant = 0
    acum = 0
    for numero in range (len(lista_numeroes_enteros)):
        cant += 1
        acum += lista_numeroes_enteros[numero]
        
    promedio = acum / cant
    return promedio

promedio = calcular_promedio_enteros(lista_numeroes_enteros)
print (f"el promedio de los numeros es {promedio}")
#2

def calcular_promedio_positivos (lista: list)->float:
    cant = 0
    acum = 0
    for numero in range(len(lista)):
        if lista[numero]>= 0:
            acum += lista[numero]
            cant += 1
            print (f"encontre {lista[numero]}")
    promedio = acum / cant
    return promedio

promedio = calcular_promedio_positivos (lista_numeroes_enteros)
print (promedio)

#3

def calcular_producto_total(lista)->float:
    acum = 1
    for indice in lista:
        acum *= indice
    return acum

prodcuto = calcular_producto_total(lista_numeroes_enteros)
print(prodcuto)
#4

def encontrar_maximo (lista):
    numero_max = lista[0]
    lista_indices_max = []
    for numero in range(len(lista)):
        numero_actual = lista[numero]
        if numero_actual > numero_max:
            numero_max = numero_actual
            lista_indices_max =[numero] 
        elif numero_actual == numero_max:
            lista_indices_max.append(numero)
    return lista_indices_max
#5 
def mostrar_indices_maximos(lista:list):
    for indice in range(len(lista)):
        print (f"los indices hallados son: {lista[indice]}")
indice = encontrar_maximo(lista_numeroes_enteros)
mostrar_indices_maximos(indice)
#6
lista = ["romina", "puca", "ejo"]
def reemplazar_nombres(lista_nombres: list, nombre:str, nombre_remplazo:str):
    cambios_realizados = 0
    print (lista)
    for indice in range(len(lista_nombres)):
        print(lista_nombres[indice])
        if lista_nombres[indice] == nombre:
            print (lista_nombres[indice])
            lista_nombres[indice] = nombre_remplazo
            print (lista_nombres[indice])
            cambios_realizados += 1
    print (f"los cambios realizados fueron {cambios_realizados} ")
    print (lista)
reemplazar_nombres(lista, "puca", "yesica")