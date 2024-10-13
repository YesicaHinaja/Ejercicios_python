matriz = [[1,2,3],[1,2,3],[1,2,3]]
matriz2 = [[1,2,3],[1,2,3],[1,2,3]]

def sumar_matrices (matriz1, matriz2)->list[list]:
    matriz_resultado = []
    for indice in range(len(matriz1)):
        lista_resultado = []
        sum = 0
        for sub_indice in range(len(matriz2[0])):
            for indice_comun in range(len(matriz1[0])):
                sum = matriz1[indice][indice_comun] + matriz2[indice][indice_comun]
