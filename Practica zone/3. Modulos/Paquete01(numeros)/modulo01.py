#UN MODULO ES UN ARCHIVO.PY QUE CONTIENE CODIGO ESPECIFICO PARA QUE NUESTRO PROGRAMA ESTE MAS ORGANIZADO

"""
en este caso usaremos este modulo para definir funciones que podremos importar
en otro archivos asi poder retulizar todo este codigo y no volver a copiar todo de nuevo porque no.

"""

def mostrarsuma (numeroA = 2, numeroB = 2):
    suma = numeroA + numeroB

    print (suma)

def mostrarmensaje ():
    print ("ESTAS DENTRO DEL MODULO UNO, Y SINO LO IMPORTASTE EE")



if __name__ == "__main__":
    print("-------------------Este número debería aparecer solo cuando ejecutes modulo01.py directamente.---------------")
    mostrarsuma()
    mostrarmensaje()
