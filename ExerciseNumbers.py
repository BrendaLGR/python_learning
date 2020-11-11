#Pedirle al usuario cuántos números sumar, y en un ciclo pedirle esos números, 
#acumular o sumar esos números en una variable y al final mostrar el resultado.


print("Suma de números")

print ('\n')

numero = int(input("Escribe cuantos números quieres sumar"))

suma = 0

for i in range(numero):

	nro = int(input("Numero: "))
	
	suma = suma+nro
	
print("La suma de los números es: ", suma)