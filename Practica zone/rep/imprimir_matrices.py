from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

#recorrer matrices en busca de un dato
def imprimir_datos_heroes(matriz: list[list], indice_fila: int):
    for fila in matriz: 
        print(fila[indice_fila])

#recorrer matrices en busca de un dato
def imprimir_datos_heroes(matriz: list[list], indice_fila: int):

    texto = ''
    
    for fila in matriz: 
        print(fila[indice_fila])

if __name__ == '__name__':
    imprimir_datos_heroes(matriz_data_heroes, 4)