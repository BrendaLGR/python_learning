#6. Hacer un script que sume las primeras 100 raices cuadradas.
#suma = raiz(1) + raiz(2) + raiz(3) ... raiz(100)
#Python ya provee una función para calcular raices cuadradas (math module)

import math

suma = 0

n1 = int(input('Numero inicial: '))
n2 = int(input('Numero final: '))

for i in range(n1, n2+1):
	solucion = math.sqrt(i)
	suma += i
print('\n La suma es: ', suma)