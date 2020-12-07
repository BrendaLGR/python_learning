#Crear una función que reciba una lista y un número y que regrese True si el número está en la lista, False si no lo está.

#La función any de Python con str.isdigit para comprobar si una cadena contiene un número

lista = [1, 2, 3, 4, 6, 7, 8, 10]

n = int(input("Escribe un numero: "))

def test_prime(n, lista):

    if (n in lista):

        return True
        print(test_prime(n,lista))

    else:

        return False
        print(test_prime(n,lista))

print(test_prime(n,lista), "En la lista")