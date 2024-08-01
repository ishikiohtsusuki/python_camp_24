# # import random
# # name=["joe","berry","bob","stuart"]
# # for i in range(len(name)):
# #   name1=random.choice(name)
# #   name1=name.remove(name1)

# colors = ["black","white","blue","purple","yellow"]
# for i in range(len(colors)):
#   print(colors[i])
#   if colors[i]=="white":
#     print(i+1)
#   if i==0 or i==2 or i==4:
#     print(colors[i])
import os as dog
from re import T
import random as stupid

words = ["dog", "urmom", "horse", "labtop", "fishs"]
word = stupid.choice(words)
lives = 5
blank = []
for i in range(len(word)):
  blank.append("_")

while lives > 0 and "".join(blank) != word:
  print("you have", lives, "lives remaining.")
  print("".join(blank))
  guess = input("guess a letter:")
  change = False
  for i in range(len(word)):
    if word[i] == guess:
      blank[i] = guess
      change = True
  if change == False:
    lives = lives - 1
  dog.system("clear")
  print("you have", lives, "lives remaining.")
  print("".join(blank))
if lives > 0:
  print("nice job")
else:
  print("try again")
