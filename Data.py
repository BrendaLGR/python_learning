## Los siguientes ejercicios se realizan para explicar el uso de Diccionario de datos

##Es una estructura de datos un tipo de datos en Python con caracteristicas
##especiales que nos permiten almacenar cualquier tipo de valor como enteros,
##cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten
##además identificar cada elemento por una clave(Key)


##Como primer ejemplo tenemos un diccionario general con diferentes conceptos y vamos a exceder a el

person_info = {'nombre': 'Brenda', 'edad': 25, 'carrera': 'TICs' }

print (person_info['nombre'])
print (person_info['edad'])
print (person_info['carrera'])


print('\n\n')

##Listado dentro de un diccionario de datos

medicines = {'medicamentos': ['Paracetamol', 'Ketorolaco','Ibuprofeno','Naproxeno']}

print (medicines['medicamentos'][3])
print (medicines['medicamentos'][2])
print (medicines['medicamentos'][1])
print (medicines['medicamentos'][0])

print('\n\n')
##For para recorrer todo el listado de medicamentos

for key in medicines:
	print (key, ":", medicines[key])

print('\n\n')

##Zip recibe elementos iterables, ya sea una cadena, una lista o una tupla.

name = ('Brenda','Leo','Edgar')
first_name = ('Gutierrez','Ramirez','Gonzalez')

x = zip(name, first_name)
print (tuple(x))