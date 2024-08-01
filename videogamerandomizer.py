# fruit = ['banana','orange','apple','pinnaple','mango']
# print(fruit[0])
# print(fruit[4])
# fruit.append('jeff')
# print(fruit)
import random
video_games = ["fortnite","call of duty","rocket leage","roblox"]
emojis = ['🏰🌜',"📞💩","🚀🍃","🛣️🧊"]
for i in range(len(video_games)):
  randomqueston = random.randint(0,len(video_games)-1)
  print(emojis[randomqueston])
  guess = input("Guess The Video Game.").lower()
  if guess == video_games[randomqueston].lower():
    print('good job.')
    score = score+1
  else:
    print('incorrect.')
  video_games.pop(randomqueston)
  emojis.pop(randomqueston)
print("lets see how you did!")
Print("your score was:",score)