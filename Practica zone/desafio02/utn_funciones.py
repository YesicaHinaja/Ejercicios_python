from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones import (
    saludo, clear_console, play_sound)

from UTN_Heroes_Dataset.utn_funciones.auxiliares import (
    color_text, crear_enunciado_desafio_1, crear_enunciado_desafio_2)


#teniendo en cuenta q cada columan representa un heroe

""""def mostrar_nombres_heroes(matriz):
    lista_nombres = matriz[0]
    lista_2 = matriz[1]
    lista_3 =matriz[2]
    lista_4 =matriz[3]
    lista_5 =matriz[4]

    for indice in range(len(lista_nombres)):
        texto = f'{lista_nombres[indice]:20} |'
        texto2 = f"{lista_2[indice]:60} | "
        texto3 = f"Apodo: {lista_3[indice]} | "
        texto4 = f"genero: {lista_4[indice]} | "
        texto5 = f"poder: {lista_5[indice]} | "
        print (texto+texto2+texto3+texto4+texto5)

mostrar_nombres_heroes(matriz_data_heroes)"""


"""def mostrar_lista_formateada (matriz:list[list]):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for sub_indice in range(columnas):
        texto = " "
        for indice in range(filas):
            texto += f"{matriz[sub_indice][indice]}"
        print(texto)
    
def mostrar_lista_formateada2(matriz: list[list]):
    filas = len(matriz[0])
    columnas = len(matriz)
    
    for fila in range(filas):  # Iterar sobre las filas
        texto = ""  # Inicializamos la variable 'texto' en cada iteración
        for columna in range(columnas):  # Iterar sobre las columnas
            texto += f"{matriz[columna][fila]} | "  # Concatenamos los elementos de cada columna
        print(texto)  # Imprimir la fila completa

mostrar_lista_formateada2(matriz_data_heroes)"""

def mostrar(matriz):
    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])
    for columna in range (cant_columnas): #RECORRE CADA COLUMNA
        texto = ""
        for fila in range(cant_filas): #RECORRE CADA FILA
            texto += f"{matriz[fila][columna]} | " #TOMA EL DATO HUBICADO EN EL MISMO INDICE Y CONCATENA HASTA TERMINAR EL FOR ir con la sigueinte columna
        print (texto)

mostrar(matriz_data_heroes)



"""def mostrar_lista_formateada(matriz: list[list]):
    filas = len(matriz[0])  # Las filas vienen de la longitud de las sublistas (nombre, apodo, etc.)
    columnas = len(matriz)  # Las columnas son la cantidad de listas (nombres, apodos, edades, etc.)
    
    for fila in range(filas):  # Iteramos sobre la cantidad de personajes (filas)
        texto = ""  # Inicializamos la variable 'texto' en cada iteración
        for columna in range(columnas):  # Iteramos sobre las listas (columnas: nombres, apodos, edades)
            texto += f"{matriz[columna][fila]} "  # Concatenamos los elementos de cada lista
        print(texto)  # Imprimir la fila completa con el personaje
mostrar_lista_formateada(matriz_data_heroes)"""