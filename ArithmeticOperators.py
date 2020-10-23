##Un python script donde se muestre el uso de los operadores aritméticos: * / - + y **

class calculadora():

	print ("Bienvenido, a continuación te muestro las opciones")

	print ('\n')

	print ("1.Suma")
	print ("2.Resta")
	print ("3.Division")
	print ("4.Exponente")
	print ("5.Multiplicacion")
	print ("6.Salir")

	print ('\n')

	opc = int(input("Por favor selecciona una opcion:  "))

	print ('\n')

	if opc == 6:
		print ("Gracias por entrar a la calculadora")
	else:
		num1 = int(input("Ingrese el primer número:  "))
		num2 = int(input("Ingrese el segundo número:  "))

		if opc == 1:
			print ("La Suma es:  ",num1+num2)
		elif opc == 2:
			print ("La Resta es:  ",num1-num2)
		elif opc == 3:
			print ("La Division es:  ",num1/num2)
		elif opc == 4:
			print ("La Potencia es:  ",num1**num2)
		elif opc == 5:
			print ("La Multiplicacion es:  ",num1*num2)
	print ("Gracias por usar mi calculadora")
