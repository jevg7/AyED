#Agregar nombres de x cantidad de estudiantes

list_estudents = list()

def add_estudents():
    student = input("Ingrese el nombre del estudiante: ")
    list_estudents.append(student)

def show_estudents():
    print("Lista de estudiantes:")
    for student in list_estudents:
        print(student)

while True:
    add_estudents()
    show_estudents()
    if input("Desea agregar otro estudiante? (s/n): ") == "n":
        break

print("Gracias por usar el programa")