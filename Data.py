## Los siguientes ejercicios se realizan para explicar el uso de Diccionario de datos

##Es una estructura de datos un tipo de datos en Python con caracteristicas
##especiales que nos permiten almacenar cualquier tipo de valor como enteros,
##cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten
##además identificar cada elemento por una clave(Key)


##Como primer ejemplo tenemos un diccionario general con diferentes conceptos y vamos a exceder a el

data = {'nombre': 'Brenda', 'edad': 25, 'carrera': 'TICs' }

print (data['nombre'])
print (data['edad'])
print (data['carrera'])


print('')
print('')
print('')

##Listado dentro de un diccionario de datos

data2 = {'medicamentos': ['Paracetamol', 'Ketorolaco','Ibuprofeno','Naproxeno']}

print (data2['medicamentos'][3])
print (data2['medicamentos'][2])
print (data2['medicamentos'][1])
print (data2['medicamentos'][0])

print('')
print('')
print('')
##For para recorrer todo el listado de medicamentos

for key in data2:
	print (key, ":", data2[key])

##Zip recibe elementos iterables, ya sea una cadena, una lista o una tupla.

data3 = zip('Brenda',[1,2,3,4,5,6])
	print (data3['Brenda'])