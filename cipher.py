word="jOMom"
alphabet= "abcdefghijklmnopqrstuvwxyz"
for i in range(len(word)):
  for letter in range(len(alphabet)):
    if word[i].lower()== alphabet[letter]:
      break
  print(alphabet[letter-1],end="")
print()
guess = input("guess the correct plaintext: ")
if guess.lower() == word.lower():
  print('correct')
if guess.lower() != word.lower():
  print('incorrect')