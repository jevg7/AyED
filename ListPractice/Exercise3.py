words = ["Hola", "paloma", "perro", "el", "ferrocarril", "playo"]


for i in range(len(words)):
    if len(words[i]) % 2 == 0:
        words[i] = words[i].upper()  
    else:
        words[i] = words[i].lower()  

print(words)