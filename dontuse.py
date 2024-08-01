# import random
# x = ["w","o","r","d"]
# did = random.shuffle(x)
# y = "".join(x)
# print(y)
# x="magma"
# magma = ["m","a","g","m","a"]
# magma[1]="?"
# magma[3]="?"
# urmom="".join(magma)
# print(urmom)
import memory
import random
import os
import time
emoji = "👍🐕🐄😂👌"
cover = '⏹️'
card_covers=[]
cards=[]
for i in range(5):
  for j in range(2):
    cards.append(emoji[i])
    card_covers.append(cover)
random.shuffle(cards)
score=0
cards=" ".join(cards)
while " ".join(card_covers).find(cover)!=-1:
  print(" ".join(card_covers))
  pair=[]
  pairspot=[]
  for i in range(2):
    guess = int(input("choose which cards you would like to reveal."))-1
    card_covers[guess] = cards[guess]
    pair.append(cards[guess])
    pairspot.append(guess)
    os.system("clear")
    print(" ".join(card_covers))
  if pair[0]!=pair[1]:
    card_covers[pairspot[0]]=cover
    card_covers[pairspot[1]]=cover
  time.sleep(1)
  os.system("clear")
if score<10:
  print("nice job!")
elif score<13:
  print("good")
else: 
  print("try again")
