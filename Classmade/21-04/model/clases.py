#Almacenar un listado de estudiantes, calcular su promedio de n clases

#Clases Basicas o modelos

class Asignatura:
    def __init__(self, nombre, descripcion, credito):
        self.nombre = nombre
        self.descripcion = descripcion
        self.credito = credito

    def __str__(self):
        return f"""Asignatura {'{'}"nombre": "{self.nombre}", "descripcion":"{self.descripcion}", "credito" : {self.credito} {'}'} """
    


asig = Asignatura("POO", "POO", 3)
print(asig)