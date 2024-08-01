import random
slots = ['😁','👌','❤️','😒','💩']
money = random.randint(100,200)
print("You have",money,"dollars.")
while money>0:
  bet = input("choose the amout of money that you would like to bet.\n")
  while bet>money:
    bet = input("only bet with the money you have. Bet again")
  slot1=random.choice(slots)
  slot2=random.choice(slots)
  slot3=random.choice(slots)
  winnings = [0]
  print(slot1,slot2,slot3)
  if slot1==slot2==slot3:
    winnings = int(bet)*5
    money = money+bet
    print("Jackpot! aww yeah! You won", winnings,"dollars worth of winnings.")
  elif (slot1==slot2) or (slot2 == slot3) or (slot3==slot1):
    print("you got a pair! you won", winnings,"dollars.")
    print("you now have",money,"dollars.")
    winnings = int(bet)*2
    money = money+winnings
    print("you have",money,"dollars")
  else:
    print("Try again!")
    money = money-int(bet)
    print("you have",money,"dollars")
  tapout = input("If you would like to tap out type tapout otherwise enter space.")
  if input == "tapout":
    break
print("you left the casino with", money, "dollars")