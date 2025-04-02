fruits = ["manzana", "banana", "kiwi", "cereza", "pera"]

char = "a"

count = [string.count(char) for string in fruits]

for i in range(len(fruits)):
    print(f"La letra '{char}' aparece {count[i]} veces en '{fruits[i]}'.")
