from model.clases import Estudiante

class Promedio:
    def __init__(self):
        self.__notas = []

    def agregar_nota(self, nota):
        self.__notas.append(nota)
    
    def calcular_promedio(self):
        suma = 0
        for nota in self.__notas:
            suma += nota.nota
        return suma / len(self.__notas)

die = Estudiante("d","d","a","i")
print (die)