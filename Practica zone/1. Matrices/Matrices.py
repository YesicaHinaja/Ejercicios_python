nombres = ["pepe", "moni", "dardo"]
edades = [56, 42, 49]
altura_cm = [175, 168, 180]


matriz_de_datos = [

    ["pepe", "moni", "dardo"], #F0
    [56, 42, 49], #F1
    [175, 168, 180]#fila2

]

#acceder a una fila
fila = 0
columna = 2

dato = matriz_de_datos[fila][columna]

#Haceder a una matris

for fila in range (len(matriz_de_datos)):

    for columna in range (len(matriz_de_datos)):
        dato = matriz_de_datos[fila][columna]
        print(f"fila: {fila} | columna: {columna} | dato: {dato}")


#inicializar una matriz

def inicializar_matriz (filas: int, columnas: int)->list[list]:
    matriz = []
    for _ in range():
        0* columnas