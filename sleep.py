import random
phrase = 'i want to go to sleep'
blanks = []
wallet = 0
wheel = [1000,800,600,400,200,0]
for i in range(len(phrase)):
  if phrase[i]==" ":
    blanks.append(" ")
  else:
    blanks.append("_")

while "_" in blanks:
  input("Press enter to spin the wheel.")
  spin = random.choice(wheel)
  if spin == 0:
    print("You are bankrupt.")
  print("you landed on",spin)
  print("".join(blanks))
  guess = input("Guess a letter.\n")
  for i in range(len(phrase)):
    if phrase[i] == guess:
      blanks[i] = guess
      wallet = wallet + spin
  print('wallet', wallet)
  print('You won! the phrase was "I want to go to sleep"')
