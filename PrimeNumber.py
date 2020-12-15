#Crear una función que reciba un número y que regrese True si el número es primo, False si no lo es.


n = int(input("Coloca un numero: "))
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True 
print("Este número es: ", is_prime(n))