# names = ["joe","jerry","bob","stuart","keven"]
# print(names[0])
# print(names[-1])
# names.append("jeff")
import random
songs = ["bejewled","message in a bottle","paper rings",'ms amaricana and the heart break prince',"london boy"]
emoji = ["🐝💎","📜➡🍼","📰💍💍","🥹🇺🇸💔🫅","🇬🇧😃"]
insults = ["you suck!","Pass it to someone who knows how to play!","what kind of guess was that!","get better!"," play this game with better wifi!","you have 0 ping and you still suck!"]
score = 0
for i in range(len(songs)):
  rq = random.randint(0,len(songs)-1)
  print(emoji[rq])
  guess = input("guess the song.")
  if guess.lower() == songs[rq].lower():
    print("good job!")
    score=score+1
  else:
    insult=random.choice(insults)
    print(insult)
  songs.pop(rq)
  emoji.pop(rq)
print("your score was",score)
if score>4:
  print("perfect score!")
elif score>3:
  print("nice job.")
else:
  print("get better!")