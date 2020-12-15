#Cómo dividir ignorando la parte fraccionaria? Investigar y subir un script .py mostrando el uso del operador //

#El cociente de una división se calcula en Python con el operador //. El resultado es siempre un número entero, 
#pero será de tipo entero o decimal dependiendo del tipo de los números empleados (en caso de ser decimal, la 
#parte decimal es siempre cero)


x = float(input("Coloque el primer número: " ))
y = float(input("Coloque el segundo número: " ))
division = x // y
print("Resultado de la division: ", division)