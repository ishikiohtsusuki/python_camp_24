import random
from termcolor import colored
words = ['bread','apple','money','adieu', 'toast','twirl','bagel','prowl','chair','magma']
word = random.choice(words)
print(word)
print(colored("welcome to wordle","light_cyan")) 
nomatch ="white"
match = "yellow"
correct = "green"

guesses = []
colors = []
for i in range(5):
  colors.append(nomatch)
for turns in range (6):
  guess = input(colored("guess a 5 letter word.\n","light_red"))
  while len(guess)!= 5 or guess in guesses:
    guess= input("guess again please \n")
  guesses.append(guess)
  for i in range(5):
    if guess[i]==word[i]:
      colors[i] = correct
    elif word.find(guess[i])>=0:
      colors[i] = match
  for i in range(len(word)):
    print(colored(guess[i],colors[i]), end=" ")
  print()
  if guess == word:
    print("nice job!")
    break