words = ["perro", "gato", "elefante", "oso", "pájaro"]


og_char = "o"
new_char = "*"


modified_words = [word.replace(og_char, new_char) for word in words]


print(modified_words)
