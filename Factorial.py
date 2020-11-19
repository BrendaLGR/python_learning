#Calcular el factorial de un número

#Un factorial se define de la siguiente manera:
#factorial_5 = 1 x 2 x 3 x 4 x 5
#factorial_3 = 1 x 2 x 3
#factorial_7 = 1 x 2 x 3 x 4 x 5 x 6 x 7


#Realizar un programa que de un output de la siguiente manera:
#n: 5
#5! = 120
#n: 8
#8! = 40320
#n: 6
#6! = 720


factorial = int(1)

numero = int(input("Inserta el numero: "))

num = numero

print("n: ",numero)

while(numero != 0):
	factorial = factorial * numero
	numero = numero -1
print (f"{num} != {factorial}")