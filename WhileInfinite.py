##En el siguiente ejercicio se pretende utilizar un While para correr una sentancia con números y si se rompe
##mostar la palabra "Feo"

import atexit ##Detecta la salida del script

class WhileInfinite():

	num = int(input("Write a number:  "))


	if num == 33:
		atexit.register (print,"Program exited successfully!")

	else:
		while num != 33:
			print("You are the ugliest")
		