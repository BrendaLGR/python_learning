#Suma de números pares del 1 al 100

suma = 0

n1 = int(input('Numero inicial: '))
n2 = int(input('Numero final: '))

for i in range (n1,n2+1):
	if i % 2 == 0:
		suma += i
print('\n La suma es: ', suma)