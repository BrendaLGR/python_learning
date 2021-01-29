#Crear un script que pasando un número como argumento lo descomponga en sus dígitos. Es decir: 642 debería ser descompuesto en:
6, 4, 2



numero = int (input("Coloca un número: "))


if(numero >= 100):
	if(numero <= 999):
		a = numero /100
		b = (numero % 100)/10
		c = (numero % 100) %10 /10
		print(a, b, c)
	else:
		print("Ese no es el numero")
else:
	print("Ese no es el numero")

