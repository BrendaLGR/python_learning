

#Como buscar un elemento X en un arreglo en Python
#Funcion que reciba un arreglo y el elemento a buscar, y que devuelva una posicion (index)
#si no se encuentra, regresar un -1 (Significa no existe)

def search(nums,x):
	if(x in nums):
		return nums.index(x)
	else:
		return -1
nums = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Escribe un número del 1 al 10: "))
print (search(nums, x))


def search1(nums, x):
	index = 0
	for i in nums:
		if i == x:
			return index
		index += 1
	return -1
nums = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Escribe un numero del 1 al 10:" ))
print (search1(nums, x))
	
