def imprimir_numero(numero:float | int)-> None: #lo ideal es q no se usea
    if type(numero) in (float, int):
        print (f"el tipo de dato de numero es {type(numero)}")
        return 1
    else: print (numero)
    return None

numero=int(input("ingrese un numero: "))
imprimir_numero(numero)
