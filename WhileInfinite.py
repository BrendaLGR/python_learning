##En el siguiente ejercicio se pretende utilizar un While para correr una sentancia con números y si se rompe
##mostar la palabra "Feo"

##import atexit ##Detecta la salida del script

#num = int(input("Escribe un numero: "))

while True:
	num = int(input("Escribe un numero: "))
	if num == 33:
		break
	else:
		print("Eres feo")