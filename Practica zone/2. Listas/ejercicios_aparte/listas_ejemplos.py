lista_falopa =  [0] * 6

for elemento in lista_falopa:
    print (elemento)


#--------------------------------------------------

lista_nombre_heroes = ["Deadpool", "Batman", "Spiderman","Goku"]

print (lista_nombre_heroes[-1]) #Muestra de atras para adelante

ultimo_indice = len (lista_nombre_heroes) - 1 #lo mismo que arroba, es otra manera de acceder a la lista

#--------------------------------------------------------------------


print (lista_nombre_heroes[1]) #muestra batman, ya que la listra empieza en la lista 0



#modificar listas usando el indice de ella



lista_nombre_heroes[0] = "Shazam"

for heroe in lista_nombre_heroes:
    print(heroe)



#agregar elementos a las listas u otro indice:
#usamos el metodo append


lista_nombre_heroes.append("saitama")

print (lista_nombre_heroes)


#La direccion de memoria:

for elemento in lista_nombre_heroes:
    print (hex(id(elemento)))



