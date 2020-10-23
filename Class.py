## En el siguiente programa se pretende realizar una clase e instanciarla


##Se crea una clase llamada humano en la cual se realizara un método para hacer referencia
##después a la instancia



class Humano(): 
    def __init__(self, edad, nombre, profesion): 
        self.edad = edad 
        self.nombre = nombre 
        self.profesion = profesion 
        

        #Creación de un nuevo método para la presentacion
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y ahora estoy {}") 
        print(presentacion.format(self.nombre, self.edad, self.profesion)) 
        
        
        #Creamos un nuevo método para cambiar la profesion:
        #En caso que esta persona sea contratada
    def contratar(self, puesto): 
        self.puesto = puesto
        print ("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.profesion = puesto 

Persona1 = Humano(25, "Brenda", "desempleada") 
#Llamamos al método
Persona1.presentar() 
print('\n\n')
Persona1.contratar("Ingeniero en Sistemas")
