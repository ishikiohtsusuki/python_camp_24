# import random
# gret=random.randint(1,10)
# if gret<5:
#   print("good night")
# else:
#   print("good morning")
# fruit = ["apple","banana","orange","mango","berry"]
# fruit = " ".join(fruit)
# print(fruit)
import random
import time
import os
bombs=[]
for i in range(3):
  bombs.append("bomb")
  bombs.append("dud")
playerlives=4
computerlives=4
turn = "player"
print("your lives:",playerlives)
print("the computers lives:",computerlives)
while computerlives>0 and playerlives>0:
  if turn=="player":
    bomb=bombs.pop(0)
    choice = input("who would you like to throw the bomb at?")
    if choice=="self":
      if bomb=="dud":
        print("you healed some")
        playerlives=playerlives+0.5
      else:
        print("you got blown up!")
        playerlives=playerlives-1
    else:
      if bomb=="dud":
        print("you gave the computer a snack!")
        computerlives=computerlives+0.5
      else:
        print('you bombed the computer!')
        computerlives=computerlives-1
    turn ="computer"
  if turn=="computer":
    choice = random.randint(1,2)
    if choice==1:
      choice1=random.randint(1,2)
      if choice1==1:
        print("the computer gave you a snack!")
        playerlives=playerlives+0.5
      else:
        print("the computer bombed you!")
        playerlives=playerlives-1
    else:
      choice1=random.randint(1,2)
      if choice1==1:
        print("the computer got a snack for themselfs!")
        computerlives=computerlives+0.5
      else:
        print("the computer bombed themselfs!")
        computerlives=computerlives-1
    turn="player"
    time.sleep(1)
    os.system("clear")
    if len(bombs)<2:
      for i in range(3):
        bombs.append("bomb")
        bombs.append("dud")
      random.shuffle(bombs)
if playerlives>0:
  print("You win!")
elif computerlives>0:
  print("computer wins!")