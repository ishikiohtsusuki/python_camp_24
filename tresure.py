import random
import time
import os
encounters=["crocodile","gecko moria","enel","rob lucci"]
sencounters=["shanks","kaido","mihawk","blackbeard"]
level=1
gold=50
turndowns=3
members=["zoro","nami","chopper","franky","brook","sanji","robin","jimbe","ussop",
print("Welcome to the Grand line adventures!")
time.sleep(1.5)
os.system("clear")
print("In this game you will be sailing the grand line.")
gmom=input("enter any button to continue")
time.sleep(0)
time.sleep(1.5)
os.system("clear")
print("there will be random encounters which you will either clear or run from.")
time.sleep.25)
os.system("clear")
print("the goal of this game is to get as much gold as you can before the end.")
time.sleep(1)
print("you will start with a ship and you will sail the sea.")
time.sleep(2)
os.system("clear")
choice = input("you have found 2 crew members, zoro and nami. Which would you like to choose to pick up for your crew?)
if choice==zoro:
  members.remove("zoro")
  print("you unlocked'zoro' and leveled up!")
else:
  members.remove("nami")
print("you unlocked 'nami' and leveled up!")
time.sleep(0.25)
print("you are curently level 2")
time.sleep(1)
level=level+1
os.system("clear")
adventure=input("You find a kindom called alabasta, and you enter. While in The city, you find a quest giver that offer's a quest for gold and to save the kingdom. Do you accept or decline?")
if adventure==accept:
  print("you go up to an evil tyrant who has been causing problems named crocodile.")
  time.sleep(1)
  print("crocadile says that to stop him, you will have to fight him.")
  time.sleep(1)
  os.system("clear")
  print("you sent crocodile flying and helped save alabasta! You go back to the quest giver and are given your gold prize, but you also unlocked the quest giver as a crew member.")
  gold=gold+100
  level=level+1
  members.remove("robin")
  time.sleep(3)
  print("you gained: 1 level, 100 gold, and 1 crew member.")
  time.sleep(1)
  os.system("clear")
  encounters.remove("crocodile")
else:
  turndowns=turndowns-1
time.sleep(0.25)
print("at sail")
time.sleep(3)
os.system("clear")
print("you come across an island, and you decide to restock on items there.")
gold=gold-5
time.sleep(1)
os.system("clear")
print("the villagers of the island bring you into a portal that teleports you into an island on the sky.")
time.sleep(2)
print("the villagers inform you about a god who has destroyed their home, and send you on a quest to stop them.")
time.sleep(2)
os.system("clear")
enel=input("you find the god in a forbidden section of the island, and challenge them.Enter anything to continue.")
if level>2:
  print("you beat up the god and sent them into space!")
  time.sleep(0.75)
  print("the people reward you with the stolen gold.")
  time.sleep(0.75)
  print("you gained: 1 level, and 150 gold.")
  time.sleep(1)
  level=level+1
  gold=gold+150
  os.system("clear")
  print("your level is:",level)
  print("your gold is",gold)
  time.sleep(1.5)
  os.system("clear")
  encounters.remove("enel")
else:
  chances=random.randint(1,3)
  if chances==1:
    print("you got smoked!")
    time.sleep(0.25)
    print("game over")
    time.sleep(0.25)
    return
  else:
    print("you beat up the god and sent them into space!")
    time.sleep(0.75)
    print("the people reward you with the stolen gold.")
    time.sleep(0.75)
    print("you gained: 1 level, and 150 gold.")
    time.sleep(1)
    level=level+1
    gold=gold+150
    os.system("clear")
    print("your level is:",level)
    print("your gold is",gold)
    time.sleep(1.5)
    os.system("clear")
    encounters.remove("enel")
time.sleep(0.25)
print("at sea...")
time.sleep(3)
os.system("clear")
rande=random.choice(encounters)
if rande=="rob lucci":
  print("You find an island with tons of cool boats and stuff")
  rob=input("would you like to visit this island?")
  if rob=="yes":