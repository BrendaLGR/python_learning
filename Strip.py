##El siguiente ejercicio pretende comprender como eliminar los espacios en blancos de un string,
##para ello existe una funcion "strip()" que a continuación se presenta:

##Cualquier objeto de tipo string implementa el método strip(). Este método se utiliza para eliminar
##todo los espacios en blanco iniciales y finales de una cadena. También toma en cuenta los tabulado-
##res y saltos de línea. Este devuelve una copia de la cadena con los caracteres iniciales y finales
##en blanco eliminados.

text =' \t\t\n\tHola \n '
print (text)

print ("")

textStrip = text.strip()
print (textStrip)


print ('')
print ('')

##Además del método strip existe rstrip() y lstrip(), estos regresan una cadena con los espacios en
##blanco del final eliminados. Por el contrario, Istrip() devuelve una cadena sin espacios en blanco
##al principio.

print ("rstrip y lstrip")
print('')

text1 =' \t\t\n\tHola \n '
print(text1)

print('')

print (text1.rstrip())

print('')

print (text1.lstrip())