

#Como buscar un elemento X en un arreglo en Python
#Funcion que reciba un arreglo y el elemento a buscar, y que devuelva una posicion (index)
#si no se encuentra, regresar un -1 (Significa no existe)


num = [1,2,3,4,5,6,7,8,9,10]

opc = int(input("Escribe un numero del 1 al 10: "))


if (opc in num):
	print ("El numero se encuentra en la posicion: ", num.index(opc))
else:
	print ("No esta en la lista -1") 
