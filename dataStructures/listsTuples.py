#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #aqui estan todos los elementos de la lsita determinados#
#input()
print(my_lista)
print(type(my_lista)) 
print(my_lista[2]) #aqui me va a mostrar hasta que numero de la lista tenemos osea va hasta el elemento 2#

print("my_lista size: ", len(my_lista)) #nos muestra el tamaño de estas#
print(my_lista[0:2])#aqui nos diga que se va mostrar desde el elemento 0 a el elemento 2 no lo incluye#
print(my_lista[:2])# nos muestra que esta lsita inicia desde cero hasta elemento numero 2 pero sin incluirlo #

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista) #muestra la lista #

my_lista.insert(3, 'Negro') # se pone este elemento en  el numero de casilla que se indica ahi#
print(my_lista) # muestra la lista# 


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)#mostrar la lista#

print(my_lista.index('Azul')) # busca la posicion donde esta azul#

#my_lista.remove('Magenta')
my_lista.remove('Marron') # busca este elemento en la lista sino esta lo elimina#
print(my_lista)

my_lista.insert(8, 'Marron') # agrega el color marron en la posicion numero 8 #
print(my_lista)

print(my_lista.pop()) # elimina y devuelve al ultimo elemento de la lista#
size = len(my_lista) #cantidad de elementos en una lista#
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #muestra los elemento 3 veces # 
print("my_lista_3: ", my_lista_3) # mostrar la lista#

print("Sort:") # ordenar la lista # 
print()
my_listaSort = my_lista.sort()
print(my_listaSort) # mostrar la lisra

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
