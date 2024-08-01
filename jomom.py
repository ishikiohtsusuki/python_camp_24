import random
# b = "plate"
# b = list(b)
# b[1] = "?"
# b[3] = '?'
# b = "".join(b)
# print(b)
word = "jomom"
word = list(word)
random.shuffle(word)
word = "".join(word)
print(word)