import random

bombs = []
for i in range(3):
  bombs.append("snack")
  bombs.append("bomb")
  random.shuffle(bombs)

playerlives = 5
computerlives = 5
turn = "player"
while playerlives > 0 or computerlives > 0:
  print("Your lives:", playerlives)
  print("Computer's lives:", computerlives)
  if turn == "player":
    bomb = bombs.pop(0)
    choice = input("who would you like to throw the bomb at?")
    if choice == "self":
      if bomb == "snack":
        print(
            " It was a snack! You ate the snack and gained 1/2 of a health point."
        )
        playerlives = playerlives + 0.5
      else:
        print("BOOM! it was a bomb!! you got blown up.")
        playerlives = playerlives - 1
    elif choice == "computer":
      if bomb == "snack":
        print(
            "it was a snack! you threw the snack, and the computer ate it. it was a 9/10 snack."
        )
        computerlives = computerlives + 0.5
        playerlives == playerlives - 0.5
    else:
      print("It was a Bomb! You bombed the computer!")
      computerlives = computerlives - 1
      turn = "computer"
  if turn == "computer":
    bomb = bombs.pop(0)
    choice = random.randint(1, 2)
    if choice == 1:
      if bomb == "snack":
        print(
            "The computer attempted to bomb you, but gave you a snack instead! the computer took emotional damage."
        )
        computerlives = computerlives - 0.5
        playerlives == playerlives + 0.5
      elif bomb == "bomb":
        print("the computer bombed you!")
        playerlives = playerlives - 1
    if choice == 2:
      if bomb == "snack":
        print("the computer ate the snack")
        computerlives = computerlives + 0.5
      if bomb == "bomb":
        print("The computer bombed themselfs!")
        computerlives = computerlives - 1
  if len(bombs) < 2:
    for i in range(3):
      bombs.append("snack")
      bombs.append("bomb")
      random.shuffle(bombs)
