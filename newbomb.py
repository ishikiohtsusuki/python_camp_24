# import random
# bomb = "💣"
# safe="😅"
# blank="⬜"
# board = []
# player1=input("player1 enter your name")
# player2=input("player 2 choose your name")
# for i in range(10):
#   board.append(blank)
# print("".join(board))
# bl=random.randint(0,9)
# while True:
#   pl= int(input(player1+"choose a location which you would like to step on."))-1
#   if pl == bl:
#     board[pl] = bomb
#     print("".join(board))
#     break
#   else:
#     board[pl]=safe
#     print("".join(board))
#   p2 = int(input(player2+"choose a location which you would like to step on."))-1
#   if p2 == bl:
#     board[p2] = bomb
#     print("".join(board))
#     break
#   else:
#     board[p2] = safe
#     print("".join(board))
# if pl == bl:
#   print(player2 +"wins!")
# else:
#   print(player1+ "wins!")
frinds = 0
family = [1, 2, "g", 4, 5]
print(family[0])
print(family[4])
if family[2] == "g":
  print("no")
else:
  print(family[2])
