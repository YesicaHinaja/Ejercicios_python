
numeros_de_la_quinierla = [0, 87, 5, 14, 48, 91]

#sumar y sacar su promedio

def sumar (lista: list)->int:
    for numero in numeros_de_la_quinierla:
        suma += numero
    return suma


def calcular_promedio (lista:list) -> float:
    cantidad_numeros = len(numeros_de_la_quinierla)
    suma = sumar(numeros_de_la_quinierla)
    promedio = suma / cantidad_numeros
    return promedio


promedio_numeros = calcular_promedio (numeros_de_la_quinierla)
print (promedio_numeros)
