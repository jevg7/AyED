#Almacenar 10 numeros enteros

list_odd = list()

def add_odd():
    odd = int(input("Ingrese un numero impar: "))

    if odd % 2 != 0 and odd >18:
        list_odd.append(odd)
        
    else:
        print("El numero ingresado no es impar o mayor de 18")
    
def show_odd():
    print("Lista de numeros impares:")
    for odd in list_odd:
        print(odd)

for i in range(10):
    add_odd()

show_odd()