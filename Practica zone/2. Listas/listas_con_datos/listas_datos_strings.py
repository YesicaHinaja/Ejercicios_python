ciudades = ["Madrid", "París", "Londres", "Berlín", "Roma"]
frutas = ["Manzana", "Banana", "Naranja", "Fresa", "Uva"]
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja"]
animales = ["Perro", "Gato", "Elefante", "Tigre", "León"]
paises = ["España", "Francia", "Alemania", "Italia", "Brasil"]


bts_miembros = [
    ["RM", "Namjoon", 1994, 30],
    ["Jin", "Worldwide Handsome", 1992, 32],
    ["Suga", "Agust D", 1993, 31],
    ["J-Hope", "Hobi", 1994, 30],
    ["Jimin", "Mochi", 1995, 29],
    ["V", "Tae", 1995, 29],
    ["Jungkook", "JK", 1997, 27]
]


for fila in bts_miembros: 
    for columna in fila:
        print(columna, end= " ")
    print()


def inicializar_matriz(contidad_filas, cantidad_columnas, valor_inicial: any )-> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial]* cantidad_columnas

        matriz = matriz + [fila]
    return matriz
















#recorremos listas:

"""
for indice in (range(len(ciudades))):
    print (ciudades[indice])



lista_vacia = []
for _ in range (7):
    nombres_bts = input("ingrese el nombre de un bts: ")
    lista_vacia.append(nombres_bts)

print (lista_vacia)

#siempre inicializar fuera
lista_frutas_no_banana = []
cont_fru = 0
for indice in range(len(frutas)):
    if frutas[indice] == "Banana":
        print (f"esta fruta se encontraba en el indice de la lista: {indice} -> {frutas[indice]}")
    else:

        lista_frutas_no_banana.append(frutas[indice])
    
for fruta in lista_frutas_no_banana:
    print (f"las frutas q no son bananas son estas: {fruta}")
        
"""







