#1 
def validar_entrada(opcion: str,num_min:int, num_max:int):
    if not opcion or  int(opcion)<num_min or int(opcion) >num_max:
        print ("error in function")
        retorno = False
    else: retorno = True
    return retorno

def llenar_matriz ()->list[list]:
    matriz = [[],[],[],[],[],[],[]]
    for lista in range(len(matriz)):
        for _ in range (3):
            print (f"ingrese la temperatura de cada hora para el dia: {lista}:")
            numero = input ("ingrese un numero: ")
            validacion = validar_entrada(numero, num_min=-10,num_max=40 )
            if validacion == True:
                matriz[lista].append(int(numero))
                print (matriz[lista])
            else: print ("error")
    return matriz

matriz = llenar_matriz()
print (matriz)


def encontrar_temp_mas_alta(matriz):
    temperatura_mas_alta = matriz[0][0]
    for indice in range(len(matriz)):
        for sub_indice in range(len(matriz[0])):
            temperatura_actual = matriz[indice][sub_indice]
            if temperatura_actual > temperatura_mas_alta:
                temperatura_mas_alta = temperatura_actual
    return temperatura_mas_alta

tem_mas_alt=encontrar_temp_mas_alta(matriz)
    
def encontrar_temp_mas_baja(matriz):
    temperatura_mas_baja = matriz[0][0]
    for indice in range(len(matriz)):
        for sub_indice in range(len(matriz[0])):
            temperatura_actual = matriz[indice][sub_indice]
            if temperatura_actual > temperatura_mas_baja:
                temperatura_mas_baja= temperatura_actual
    return temperatura_mas_baja

def calcular_promedio_dia(matriz: list[list]):
    lista_promedio_dias = [[],[],[],[],[],[],[]]
    HORAS = 3
    for indice in range(len(matriz)):
        acum_dias = 0
        for sub_indice in range(len(matriz[0])):
            acum_dias += matriz[indice][sub_indice]
        promedio_dia = acum_dias / HORAS
        lista_promedio_dias[indice].append(promedio_dia)
    return lista_promedio_dias

lista = calcular_promedio_dia (matriz)
print(f"la listra es: {lista}")

