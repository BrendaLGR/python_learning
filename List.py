##Hacer un programa en el que se asigne una lista de 10 elementos, (no importa el tipo)
##y se modifique el primer elemento y el último, luego se muestren todos los elementos 
##uno por uno con un for.

class List():

	num_list = [1,2,3,4,5,6,7,8,9,10]

	print(num_list)

	num_list.pop(0)

	print(num_list)

	num_list.insert(0, 11)

	print(num_list)

	num_list.pop(5)

	print(num_list)

	num_list.insert(9, 12)

	print(num_list)

	print ('\n')

	for i in num_list:
		print (i)

