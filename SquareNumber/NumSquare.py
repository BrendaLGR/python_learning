def squareNum(base, resultado, i, exponente):
    while i <= exponente:
        resultado = resultado * base
        i = i+1
    return resultado
base = int(input("Escribe un numero de base: "))
exponente = int(input("Escribe el numero de exponente: "))
i = 1
resultado = 1
print (squareNum(base, resultado, i, exponente))