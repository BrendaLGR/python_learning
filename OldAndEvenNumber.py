#Hacer un script que le pida al usuario un número y le diga si el número que ingresó es par o impar.
#Para los ejercicios 2 y 3 se debe crear una función para cada uno, es decir, una función que reciba 
#un número y regrese True si es par o False si es impar.


num = int(input("Ingrese el numero: "))

if num % 2 == 0:
	num = True
	print("El numero es par: ", True)
else:
	num = False
	print("El numero es impar:", False)