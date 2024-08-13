import random
import time
import os
# from display import show_img, show_mov
from pip import pillow
# show_img("jomomomm.webp", 2)
# # show_mov(".mp4", 3)

def one_piece():
  encounters = ["crocodile", "gecko moria", "enel", "rob lucci"]
  sencounters = ["shanks", "kaido", "mihawk", "blackbeard"]
  level = 1
  gold = 50
  turndowns = 3
  coolness=0
  members = [
    "zoro", "nami", "chopper", "franky", "brook", "sanji", "robin",
    "jimbe", "ussop"
  ]
  print("Welcome to the Grand line adventures!")
  # show_img("jomomomm", 2)
  time.sleep(2)
  os.system("clear")
  print("In this game you will be sailing the grand line.")
  input("enter any button to continue")
  time.sleep(2)
  os.system("clear")
  print(
    "there will be random encounters which you will either clear or run from."
  )
  time.sleep(4)
  os.system("clear")
  print("the goal of this game is to get as much gold as you can before the end.")
  time.sleep(3)
  print("you will start with a ship and you will sail the sea.")
  time.sleep(4)
  os.system("clear")
  choice = input(
    "you have found 2 crew members, zoro and nami. Which would you like to choose to pick up for your crew?"
  )
  if choice == "zoro":
    members.remove("zoro")
    print("You unlocked'zoro' and leveled up!")
  else:
    members.remove("nami")
    print("You unlocked 'nami' and leveled up!")
  time.sleep(2)
  print("you are currently level 2")
  time.sleep(2)
  level = level + 1
  os.system("clear")
  adventure = input(
    "You find a kindom called alabasta, and you enter. While in The city, you find a quest giver that offer's a quest for gold and to save the kingdom. Do you accept or decline?"
  )
  time.sleep(1)
  os.system("clear")
  if adventure == "accept":
    print(
      "you go up to an evil tyrant who has been causing problems named crocodile."
    )
    time.sleep(1)
    print("crocadile says that to stop him, you will have to fight him.")
    time.sleep(1)
    os.system("clear")
    print(
      "you sent crocodile flying and helped save alabasta! You go back to the quest giver and are given your gold prize, but you also unlocked the quest giver as a crew member."
    )
    gold = gold + 100
    level = level + 1
    members.remove("robin")
    time.sleep(5)
    os.system("clear")
    print("you gained: 1 level, 100 gold, and 1 crew member.")
    time.sleep(1)
    os.system("clear")
    encounters.remove("crocodile")
  else:
    turndowns = turndowns - 1
  time.sleep(0.25)
  print("at sail")
  time.sleep(3)
  os.system("clear")
  print(
    "you come across an island, and you decide to restock on items there.")
  gold = gold - 5
  time.sleep(2)
  os.system("clear")
  print(
    "the villagers of the island bring you into a portal that teleports you into an island on the sky."
  )
  time.sleep(4)
  print(
    "the villagers inform you about a god who has destroyed their home, and send you on a quest to stop them."
  )
  time.sleep(4)
  os.system("clear")
  enel = input(
    "you find the god in a forbidden section of the island, and challenge them.Enter anything to continue."
  )
  time.sleep(0.25)
  os.system("clear")
  print("battlng...")
  time.sleep(2)
  os.system("clear")
  if level > 2:
    print("you beat up the god and sent them into space!")
    time.sleep(0.75)
    print("the people reward you with the stolen gold.")
    time.sleep(0.75)
    print("you gained: 1 level, and 150 gold.")
    time.sleep(1)
    level = level + 1
    gold = gold + 150
    os.system("clear")
    print("your level is:", level)
    print("your gold is", gold)
    time.sleep(1.5)
    os.system("clear")
    encounters.remove("enel")
  else:
    chances = random.randint(1, 3)
    if chances == 1:
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
      level = level + 1
      gold = gold + 150
      os.system("clear")
      print("your level is:", level)
      print("your gold is", gold)
      time.sleep(1.5)
      os.system("clear")
      encounters.remove("enel")
  time.sleep(0.25)
  print("at sea...")
  time.sleep(3)
  os.system("clear")
  rande = random.choice(encounters)
  while encounters != "[]":
    if rande == "rob lucci":
      print("You find an island with tons of cool boats and stuff")
      rob = input("would you like to visit this island?")
      if rob == "yes":
        time.sleep(1)
        os.system("clear")
        print(
          "your ship broke down! you will have to repair your ship.")
        time.sleep(2)
        os.system("clear")
        frank = input(
          "you find a mysterious person offering you a new ship for 50 gold and someone else to repair your old ship for 30 gold. which do you choose mystery or normal repair?"
        )
        if frank == "mystery":
          gold = gold - 50
          members.remove("franky")
          level = level + 1
          time.sleep(0.3)
          os.system("clear")
          print("you got a new ship, a crew member and a level up!")
          time.sleep(2)
          print("charecter unlock: franky.")
          time.sleep(2)
          os.system("clear")
        else:
          print("your boat got repaired.")
          gold = gold - 50
        time.sleep(0.4)
        print(
          "you find that people have snuck into the palace and are attempting to steal the kings gold!"
        )
        time.sleep(2)
        os.system("clear")
        robn = input("the villigers ask you for your help. yes or no?")
        if robn == "yes":
          time.sleep(0.25)
          print(
            "you go up to confront the person named rob lucci who has been causing the problems."
          )
          time.sleep(2)
          os.system("clear")
          print("rob lucci starts attacking you!")
          if level > 4:
            time.sleep(1)
            os.system("clear")
            print(
              "you beat up rob lucci and the king rewards you with some of his gold."
            )
            encounters.remove("rob lucci")
            time.sleep(3)
            print("you got 100 gold and a level up!")
            level = level + 1
            gold = gold + 100
            print("your level is", level)
            print("you have", gold, "gold.")
          elif level > 3:
            gomomom = random.randint(1, 2)
            if gomomom == 1:
              time.sleep(1)
              print("you lose!")
              return
            else:
              time.sleep(1)
              os.system("clear")
              print("you beat up rob lucci and steal his money!")
              encounters.remove("rob lucci")
              print("you got 100 gold and a level up!")
              level = level + 1
              gold = gold + 100
              print("your level is", level)
              print("you have", gold, "gold.")
      print("you set sail")
      time.sleep(3)
    elif rande == "crocodile":
      os.system("clear")
      adventure = input(
        "You find a kindom called alabasta, and you enter. While in The city, you find a quest giver that offer's a quest for gold and to save the kingdom. Do you accept or decline?"
      )
      time.sleep(1)
      os.system("clear")
      if adventure == "accept":
        print(
          "you go up to an evil tyrant who has been causing problems named crocodile."
        )
        time.sleep(1)
        print(
          "crocodile says that to stop him, you will have to fight him."
        )
        time.sleep(1)
        os.system("clear")
        print(
          "you sent crocodile flying and helped save alabasta! You go back to the quest giver and are given your gold prize, but you also unlocked the quest giver as a crew member."
        )
        gold = gold + 100
        level = level + 1
        members.remove("robin")
        time.sleep(5)
        os.system("clear")
        print("you gained: 1 level, 100 gold, and 1 crew member.")
        time.sleep(1)
        os.system("clear")
        encounters.remove("crocodile")
      else:
        turndowns = turndowns - 1
      time.sleep(0.25)
      print("at sail")
      time.sleep(3)
      os.system("clear")
    elif rande == "gecko moria":
      bark = input("you came across an island, do you enter or skip?")
      if bark == "enter":
        time.sleep(0.3)
        os.system("clear")
        print("you enter a mysterious island...")
        time.sleep(2.5)
        print(
          "BOO! You find a mysterious talking skeleton. the skeleton inform's you that what you thought was an island was actually a ship. he tells you that he will join your crew if you help him bust some zombies.")
        time.sleep(8)
        os.system("clear")
        print("you go onto the ship blow up some zombies and are confronted by the giant zombie boss.")
        time.sleep(4)
        os.system("clear")
        time.sleep(0.25)
        print("negotiating with giant zombie...")
        time.sleep(1.5)
        os.system("clear")
        cool=random.randint(0,1)
        if cool==0:
          print("It turn's out that the zombie is just a misunderstood nice person!")
          time.sleep(3)
          os.system("clear")
          members.remove("brook")
          level=level+1
          rly=input("All the zombie wanted was a friend. You invite the zombie to join your crew and he offer's you his giant boat.do you want the new ship or keep the old one?")
          time.sleep(0.25)
          os.system("clear")
          if rly=="keep":
            print("you decide to keep your ship")
          else:
            print("you took the giant ship and sold your old one!")
            gold=gold+50
            time.sleep(2)
            print("Franky makes special edits on the new ship, making it dope.")
            time.sleep(3)
            os.system("clear")
            coolness=coolness+1
        else:
          print("it turns out the zombie is not so nice!")
          time.sleep(2)
          os.system("clear")
          print("unzombifing zombie...")
          time.sleep(3)
          os.system("clear")
          if level>6:
            print("you turned the zombie back into a nice human, but in the form of a skeleton named brook.")
            rlly=input("You invite Brook to join your crew and he offer's you his giant boat. do you want the new ship or keep the old one?")
            time.sleep(0.25)
            os.system("clear")
            if rlly=="keep":
              print("you decide to keep your ship")
            else:
              print("you took the giant ship and sold your old one!")
              gold=gold+50
              time.sleep(2)
              if "franky"in members:
                print("Franky makes special edits on the new ship, making it dope.")
              time.sleep(3)
              os.system("clear")
              coolness=coolness+1
            level=level+1
          elif level>4:
            morii=random.randint(1,3)
            if morii==1:
              print(" you lose and the zombie turn's you into a zombie!")
              time.sleep(2)
              os.system("clear")
              return
            else:
              print("you turned the zombie back into a nice human, but in the form of a skeleton named brook.")
              rlly=input("You invite Brook to join your crew and he offer's you his giant boat. do you want the new ship or keep the old one?")
              time.sleep(0.25)
              os.system("clear")
              if rlly=="keep":
                print("you decide to keep your ship")
              else:
                print("you took the giant ship and sold your old one!")
                gold=gold+50
                time.sleep(2)
                if "franky"in members:
                  print("Franky makes special edits on the new ship, making it dope.")
                time.sleep(3)
                os.system("clear")
                coolness=coolness+1
              level=level+1
    print("your level is:",level)
    print("you have",gold,"gold.")
  print("you have traveled the grand line and now are entering the new world!")
  time.sleep(3)
  input("enter anything to proceed.")
  time.sleep(0.2)
  os.system("clear")
  print("crew advancing...")
  time.sleep(2)
  os.system("clear")
  level=10
  gold=gold+50
  print("you have entered the new world!")
            
            
            

one_piece()
