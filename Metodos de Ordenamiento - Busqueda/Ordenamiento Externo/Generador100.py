import random
import string

def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generar 100 palabras aleatorias de longitud 5
for i in range(100):
    print(random_word(5))
