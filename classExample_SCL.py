""""
Consigna:

Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
from select import select


class Alumno :
    def __init__  (self, nombre="default", nota=None):
        self.nombre = nombre
        self.nota = nota
        self.apto = 0 # 0 sin calificar, -1 suspenso, 1 aprobado

    def getNombre(self):        #getter y setter
        return self.nombre

    def getNota(self):
        return self.nota

    def setNombre(self, n):
        self.nombre = n

    def setNota(self, n):
        if n>=0 and n<=10:
            self.nota = n
        else:
            print("Error, la nota debe estar entre 0 y 10")

    def evaluar(self):
        if self.nota > 5:
            return "APROBADO CON {}".format(self.nota)
            self.apto = 1
        else: 
            return "SUSPENSO CON {}".format(self.nota)
            self.apto = -1

    def __str__(self):
        return "{} con nota {}, valor de apto es {}".format(self.nombre, self.nota, self.apto)



#Probando-------------------------------------------
yo = Alumno("Sergio", 10)
print(yo.__str__())


yo.setNombre("Pedro")
print(yo.__str__())

yo.setNota(5)


        
