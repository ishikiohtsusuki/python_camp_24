import random
import os
import time

emoji = "👍🐕🐄😂👌"
cover = '⏹️ '

card_covers = []
cards = []

for i in range(5):
  for j in range(2):
    cards.append(emoji[i])
    card_covers.append(cover)
random.shuffle(cards)
guesses = 0
cards = "".join(cards)

while cover in card_covers:
  print("".join(card_covers))
  pair = []
  guesses = guesses + 1
  for p in range(2):
    guess = int(input("Pick a card, any card.\n")) - 1
    card_covers[guess] = cards[guess]
    pair.append(guess)
    os.system("clear")
    print("".join(card_covers))
  if cards[pair[0]] != cards[pair[1]]:
    card_covers[pair[0]] = cover
    card_covers[pair[1]] = cover
  time.sleep(2)
  os.system('clear')
if guesses < 8:
  print("Amazing job!!")
elif guesses < 10:
  print("GGggrrrrrEAt Job!!!")
elif guesses < 12:
  print("Nice!")
else:
  print("Pass it to someone who knowes how to play!")
print("You got a Score of", guesses)
