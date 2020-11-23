#Hacer un script que reciba un número desde la consola y diga si el número es par o impar, algo así debería ser la ejecución

num = int(input("Ingrese el numero: "))

if num % 2 == 0:
	print(f"El {num} es par")
else:
	print(f"El {num} es impar")