
def pedir_nombre ():
    nombre = input ("Ingrese su nombre: ")

    return nombre

def MostrarNombre(nombre):
    print (nombre)

if __name__ == "__main__":
    nombre = pedir_nombre()
    MostrarNombre(nombre)