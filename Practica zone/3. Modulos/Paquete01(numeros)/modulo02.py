#COMO SE DIJO ANTERIOMENTE SE PUEDEN IMPORTAR MODULOS DESDE OTRO MODULOS
#FORMAS DE IMPORTACION: 

#---------------------------FORMA 1-------------------------------------------------------------
#Importa todo el mudulo pero si queremos utilizarlo debemos acceder a una funcion, por ejemplo 
# usando el "." + la funcion que queremos usar por ejemplo: 
import modulo01   

print ("FORMA 1-----------------------------------------------")
modulo01.mostrarsuma(5,5) # aqui accedimos a la funcion mediante le punto.


#--------------------------FORMA 2---------------------------------------------------------------------
#importa solo una funcion o elemento especifico, por ejemplo: 
from modulo01 import mostrarsuma

print ("FORMA 2-----------------------------------------------")
mostrarsuma() #No es necesario usar el punto para acceder, se usa como si fuera el modulo donde se encuntra esa funcion


#------------------------FORMA 3----------------------------------------------------------------------------
#Importa VARIAS funciones o elementos de un modulo, lo mismo que la dos pero con el , podremos agregar otras funciones que necesitemos
from modulo01 import mostrarsuma, mostrarmensaje # usar el coma seguido de la otra funcion
print ("FORMA 3-----------------------------------------------")
mostrarsuma()
mostrarmensaje()

#------------------------FORMA 4 (no recomendada)---------------------------------------------------------------
#importa el modulo completo, por lo que no es recomendable usarlo. es como el modulo original pero no es la idea,
#seria como una copia pero ocultando todo mi codigo 
from modulo01 import *
print ("FORMA 4-----------------------------------------------")
mostrarmensaje()
mostrarsuma()


#----------------PLUS---------------------------------
#IMPORTAMOS EL ARCHIVO PERO CON UN ALIAS QUE PODREMOS USAR UNICAMENTE EN EL MODULO ACTUAL:

import modulo01 as funciones
print ("plus-----------------------------------------------")
funciones.mostrarsuma()  #es lo mismo que...
modulo01.mostrarsuma()   #esto 

#en este caso funciona la linea 41 solo porque importamos el archivo desde otro numero


#---------------IMPORTACION RELATIVA--------------
#es la que debe usarce en los modulos dentro de nuestros paquetes
from .modulo01 import mostrarmensaje