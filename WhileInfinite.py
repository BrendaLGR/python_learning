##En el siguiente ejercicio se pretende utilizar un While para correr una sentancia con números y si se rompe
##mostar la palabra "Feo"

##import atexit ##Detecta la salida del script

class WhileInfinite():


	n = input("N: ")

	while True:
		if n == 33:
			break
		else:
			print("Eres feo")
			
		