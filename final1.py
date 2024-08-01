import random
import os
from termcolor import colored
import time
people = ['gojo','itadori']
person = input("chose who would you like to participate as. type gojo for gojo and type itadori for itadori. anything else will result in a random person.")
gojo_moves = ["reversed cursed technique","red","hollow purple","domain expansion: infinite void"]
itadori_moves = ["reversed cursed technique","black flash","cursed energy punch","get help"]
if person == 'gojo':
  person = people[0]
elif person == 'itadori':
  person = people[1]
else:
  person = random.choice(people)
if person == people[0]:
  gojohealth = 100
  sukunahealth = 100
  print("You are Gojo.")
  print("your mission is to stop Sukuna.")
  print("you will be on this mission as gojo, try to get redemtion by outsmarting sukuna.")
  gojo1 = int(input("sukuna is attacking you! What will you do? press 1 to block and 2 to dodge."))
  time.sleep(1)
  os.system("clear")
  if gojo1 == 1:
    gojoblock1 = random.randint(0,1)
    if gojoblock1 == 0:
      print("you succsesfully blocked!")
      gojohealth = gojohealth-10    
      print("your remainin health is:",gojohealth)    
    else:
      print(colored("you got hit!","red"))
      gojohealth = gojohealth - 25
      print("your remainin health is:",gojohealth)
  else:
    gojododge1 = random.randint(0,1)
    if gojododge1 == 0:
      print("you sucsessfully dodged")
    else:
      print(colored("you got hit!","red"))
      gojohealth = gojohealth-35
      print("your remaininh health is:",gojohealth)
  print("your turn!")
  gojoturn = int(input("enter what you want to do: reverse cursed technique, or red. Press 1 for reverse cursed technique and 2 for red."))
  time.sleep(1)
  os.system("clear")
  if gojoturn == 1:
    print("you healed up some.")
    gojoreverse=random.randint(15,25)
    gojohealth = int(gojohealth) + int(gojoreverse)
    print("your remainin health is:",gojohealth)
  elif gojoturn ==2:
    sukunadodgered = random.randint(0,2)
    if sukunadodgered == 0:
      print("your red got blocked by sukuna!")
      sukunahealth = sukunahealth + 5
      print("sukuna's remaining health is:",sukunahealth)
  else:
      print(colored("you hit sukuna!","blue"))
      sukunahealth = sukunahealth -20
      print("sukuna's remaining health is:",sukunahealth)
  sukuna_attack2=int(input("sukuna is trying to suck you into his domain! what will you do?enter 2 to use your own domain,or run away in fear."))
  time.sleep(1)
  os.system("clear")
  if input == 1:
    print("you sucsessfully escaped sukuna's domain!")
  else:
    sukuna_attack2 = random.randint(0,2)
    if sukuna_attack2 == 0:
      print(colored("you cancled out sukunas domain with yours and your domain is now in play.","blue"))
      sukunahealth = sukunahealth-20
      print("sukuna's remaining health is:",sukunahealth)
    elif sukuna_attack2 == 1:
      print("you cancled each others domain's out.")
      gojohealth = gojohealth-10
      sukunahealth = sukunahealth-10
      print("your remainin health is:",gojohealth)
      print("sukuna's remaining health is:",sukunahealth)
    else:
      print(colored("sukuna's domain was sucsessful!Ow!!","red"))
      gojohealth = gojohealth-30
      print("your remainin health is:",gojohealth)
  if sukunahealth<90:
    gojopurple=int(input("You can use hollow purple if you would like to, or you can use domain amplification. type 1 for hollow purple and 2 for domain amplification."))
    time.sleep(1)
    os.system("clear")
    if gojopurple == 2:
      print("you succsesfully used the sure hit of your domain amplification!")
      sukunahealth = sukunahealth-25
      print("sukuna's remaining health is:",sukunahealth)
    else:
      gojohollow=random.randint(0,3)
      if gojohollow == 0:
        print("you were unsucsessful in your hollow purple!")
        gojohealth = gojohealth-15
        print("your remainin health is:",gojohealth)
      else:
        print(colored("you landed your hollow purple!","blue"))
        sukunahealth = sukunahealth-40
        print("sukuna's remaining health is:",sukunahealth)
        if sukuna_attack2 == 2:
          gojohealth=gojohealth-30
          print("your remainin health is:",gojohealth)
        elif sukuna_attack2 ==0:
          sukunahealth = sukunahealth-20
        print("sukuna's remaining health is:",sukunahealth)
        print("your remainin health is:",gojohealth)
        time.sleep(2)
        os.system("clear")
  else:
      gojoturn2=int(input("Your turn! would you like to use reverse cursed technique, or six eyes dash? press 2 for reverse cursed technique, and 3 for six eyes dash."))
      time.sleep(1)
      os.system("clear")
      if gojoturn2 == 2:
        gojohealth = gojohealth+10
        print("you re-gained some health.")
        print("your remaining health is:",gojohealth)
      else:
        print(colored("you six eyes dash was succsesful, but got partially blocked!","blue"))
        sukunahealth = sukunahealth-25
        print("sukuna's remaining health is:",sukunahealth)
  print("whoever has more health after next turn wins!")
  finalstandoff = int(input("choose a number 1-2 and your fate will be dicided."))
  time.sleep(1)
  os.system("clear")
  time.sleep(1)
  if finalstandoff ==1:
    sukunahealth = sukunahealth-20
    print("sukuna's remaining health is:",sukunahealth)
  else:
    gojohealth = gojohealth-20
    print("your remaining health is:",gojohealth)
  if gojohealth>sukunahealth:
    print("you won!")
    print("your remaining health is:",gojohealth)
  elif sukunahealth>gojohealth:
    print("you lost!")
    print("sukuna's remaining health is:",sukunahealth)
  else:
    print("draw!")
elif person == people[1]:
  itadorihealth = 50
  mahitohealth = 50
  print("your mission is to stop mahito.")
  print("you will be on this mission as itadori, try to prevent Mahito from getting his way.")
  time.sleep(3)
  os.system("clear")
  itadori_block1 = int(input("mahito is attempting to smack you! press 1 to block and 2 to counter."))
  time.sleep(0.5)
  os.system("clear")
  if itadori_block1 == 1:
    itadori_block1 = random.randint(0,2)
    if itadori_block1 == 1 or 2:
      print("you fully blocked!")
      mahitohealth = mahitohealth-10
      print("Mahito's remaining health is:",mahitohealth)
    else:
      print("you missed you block!")
      itadorihealth = itadorihealth-10
      print("Your remaining health is:",itadorihealth)
      time.sleep(1)
      os.system("clear")
  else:
    itadori_block1 = random.randint(0,1)
    if itadori_block1 == 0:
      print("you countered with a black flash!")
      mahitohealth = mahitohealth-20
      print("Mahito's remaining health is:",mahitohealth)
    else:
      print("you missed you counter!")
      itadorihealth = itadorihealth-20
      print("Your remaining health is:",itadorihealth)
  time.sleep(2)
  os.system("clear")
  print("your turn")
  itadoriturn = int(input("would you like to play it safe or risk it? press one to play it safe and 2 to risk it."))
  
  if itadoriturn == 2:
    print("you and mahito will take 15 damadge per input of 1 untill one of you is dead.input something else to break it.")
    time.sleep(4)
    os.system("clear")
    mahitohealth=mahitohealth-15
    itadorihealth=itadorihealth-15
    print("Mahito's remaining health is:",mahitohealth)
    print("Your remaining health is:",itadorihealth)
    battle2 = int(input("would you like to stop or keep going? press 1 to keep going."))
    time.sleep(0.5)
    os.system("clear")
    if battle2 == 1:
      while itadorihealth and mahitohealth>0:
        mahitohealth=mahitohealth-15
        itadorihealth=itadorihealth-15
  if itadorihealth and mahitohealth>0:
    print("Mahito's remaining health is:",mahitohealth)
    time.sleep(2)
    os.system("clear")
    random1 = int(input("choose a number 1 or 2, this will result if you or mahito gets to attack."))
    time.sleep(0.5)
    os.system("clear")
    random1=random.randint(1,2)
    if random1 == random.randint(1,2):
      print("your turn!")
      irandom = int(input("you have 2 choices, press 1 to use reverse cursed technique or press 2 to attempt a ultimate pow."))
      time.sleep(0.5)
      os.system("clear")
      if irandom == 2:
        irandom = random.randint(0,1)
        if irandom == 0:
          print("You hit you cursed energy ultimate pow!")
          mahitohealth = mahitohealth -20
          print("Mahito's remaining health is:",mahitohealth)
        else:
          print("you missed your ultimate pow!")
          itadorihealth = itadorihealth - 10
          print("Your remaining health is:",itadorihealth)
      else:
        print("you regained some health.")
        reverseitadori=itadorihealth+random.randint(10,20)
        itadorihealth = reverseitadori
        print("Your remaining health is:",itadorihealth)
    elif random1 == 1:
      print("Mahito gets the turn!")
      mahitodomain = int(input("mahito is using domain expantion! enter 1 too atempt to escape or 2 to use simple domain and use ultimate pow."))
      time.sleep(0.5)
      os.system("clear'")
      if mahitodomain == 2:
        simpledomain = random.randint(0,3)
        if simpledomain == 0:
          print("your simple domain failed!")
          itadorihealth = itadorihealth-10
          print("Your remaining health is:",itadorihealth)
        else: 
          print("your domain was sucsessful!")
          powpow = int(input("press any key to use ultimate pow!"))
          powpow=random.randint(0,2)
          if powpow==0:
            print("you failed to hit your ultimate pow!")
            itadorihealth = itadorihealth-5
            print("Your remaining health is:",itadorihealth)
          else:
            print("You hit your ultimate pow!")
            mahitohealth = mahitohealth - 15
            print("Mahito's remaining health is:",mahitohealth)
      time.sleep(1)
      os.system("clear")
    if itadorihealth>mahitohealth:
      print("You win!")
    elif itadorihealth<mahitohealth:
      print("You lose!")
    else:
      print("it's a tie!")
  else:
    print("it is over")
    time.sleep(1)
    os.system("clear")
    if itadorihealth>mahitohealth:
      print("You win!")
    elif itadorihealth<mahitohealth:
      print("You lose!")
    else:
      print("it's a tie!")