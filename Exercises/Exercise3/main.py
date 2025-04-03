from search_algorithms.search2 import linear_search
from search_algorithms.search1 import binary_search


numbers = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(numbers, target)

if result != -1:
    print(f"Elemento encontrado en el índice {result}")
else:
    print("Elemento no encontrado")


target = 15
numbers.sort()  
result = binary_search(numbers, target)

if result != -1:
    print(f"Elemento encontrado en el índice {result}")
else:
    print("Elemento no encontrado")
