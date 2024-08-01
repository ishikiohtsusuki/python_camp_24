# meats = ["rib", "loin","flank"]
# print(meats[2])
# print(meats[1])
# print(meats[0])
# costs = [10.99,19.99,14.99]
# print(costs[0])
# print(costs[1])
# print(costs[2])
# #these are the lists
# meats.append('rib')
# #adds to the list
# meats.pop(1)
# #removes from the list (in order)
# print(meats)
# costs.remove(10.99)
# #must be the specific number
# print(costs)
import random
bomb='💣'
safe='🤣'
board=[]
blank='😒'
for i in range(15):
  board.append(blank)
print("".join(board))
bomblocation = random.randint(0,14)
while True:
  player1 = int(input("player 1, choose the location which you would like to test."))
  if player1 == bomblocation:
    board[player1] = bomb
    print("".join(board))
    print("BOOM!!! The bomb blew you up. Player 2 wins..")
    break
  else:
    board[player1] = safe
    print("".join(board))
  player2 = int(input("player 2, choose the location which you would like to test."))
  if player2 == bomblocation:
    board[player2] = bomb
    print("".join(board))
    print("BOOM!!! The bomb blew you up. Player 1 wins.")
    break
  else:
    board[player2] = safe
    print("".join(board))
