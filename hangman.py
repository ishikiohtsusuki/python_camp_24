import random
import ascii
import os
import time
for i in range(5):
  words = ['labtop','picnic','hollow','purple','domain']
  word = random.choice(words)
  blank = []
  score = [0]
  error = 0
  for i in range(6):
    blank.append("_")
  print(" ".join(blank))
  while "_" in blank:
    guess = input("Guess a letter.\n")
    correct = False
    
    for i in range(6):
      if word[i] == guess:
        blank[i] = guess
        correct = True
    if correct == False:
      error = error+1
    os.system("clear")
    print(" ".join(blank))
    print( "the amount of times you have guessed wrong is:",error)
    print(ascii.hangman[error])
 
    print("good job!")
  if not "_" in word:
    "".join(score)
    score = score+1
    

print("game over.")
time.sleep(0.5)
print("your score was:",score,"/5")


    