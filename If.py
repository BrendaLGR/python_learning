##Los siguientes ejercicios se pretende usar el If, Else y Elif

##	1)

num= int(input("Escriba un número: "))

if num < 0:
	print("Ese número no es positivo")
print("El número que escibio es: ", num)


##	2)

edad=int(input("Escriba su edad:  "))
if edad < 18:
	print("Usted es menor de edad")
else:
	print("Usted es mayor de edad")
print("Adios")

##	3)

dedos=int(input("¿Cuántos dedos tiene el humano?"))

if dedos == 10:
	print("Dedos es igual a 10")
elif dedos == 15:
	print("Dedos es igual a 15")
elif dedos == 20:
	print("Correcto!, Dedos es igual a 20")
print("En el humano existen 20 dedos, sin embargo hay gente que tiene menos o tiene más")