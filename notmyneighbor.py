import random
import time
import os
while True:
  print(randomgreeting) = random.choice(greeting)
  time.sleep(2)
  os.system(clear)
  print(randomconversation) = random.choice(conversation)
  time.sleep(3)
  os.system(clear)
  print(randomfollowup) = random.choice(followup)
  time.sleep(3)
  os.system(clear)
  print(randomgoodbye) = random.choice(goodbye)
  time.sleep(1)
  os.system(clear)
  imposter = random.randint(1,2)
  greeting = ["yo,",'hi.','whatsup?', 'how are you?','good afternoon.'how are you?']
  conversation = ['what's your IP adress?','whats your SSN?','whats your favorite movie?','Whats your yearly income?','How old are you?','Do you have a gaming console?']
  followup = ['alright. What do you like to do during the summer?']
  goodbye = ['cya.','bye.','goodbye.','later.']
  if imposter == 1:
    randomgreeting = randomgreeting.replace('u','v')
    randomconversation = randomconversation.replace('u','v')
    randomfollowup = randomfollowup.replace('u','v')
    randomgtoodbye = randomgoodbye.replace('u','v')
  
  answer = input(" Is this an imposter?")
  if answer == yes and imposter == 1:
    print("the imposter was found guilty.")
  elif: answer == "no" and imposter ==2:
    print("youre correct, they were not an imposter!")
  else:
    print("you trusted them too much! the imposter got you!")
  time.sleep(4)
  os.system(clear)