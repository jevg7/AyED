fruits = ["manzana", "", "banana", "", "kiwi", "", "pera"]

fruits_without_voids = [fruit for fruit in fruits if fruit != ""]

print(fruits_without_voids)
