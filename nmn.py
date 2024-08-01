import random
import time
import os
alph = ['e','i','u']
score=0
greeting = ["Hi","hey there","how are you","what's good?","hello!"]
convo = ["what are some of you favorite books and movies?","what are some of your hobbies?","have you had any intereresting travels?","what have you been doing over the summer?"]
followup =["Cool!","that sounds fasinating I really wish I cared.","Sounds amazingly intereasting.","please, share some more details.","what is your social security number?","what is your credit card number and bank pin?"]
end = ["by","see you","take care","come again!"]
for g in range(6):
  imposter=random.randint(1,2)
  rg=random.choice(greeting)
  rc=random.choice(convo)
  rf=random.choice(followup)
  rs=random.choice(end)
  repl= random.randint(0,2)
  if imposter == 1:
    if repl ==0:
      rg=rg.replace("e","i")
      rc=rc.replace("e","i")
      rf=rf.replace("e","i")
      rs=rs.replace("e","i")
    elif repl == 1:
      rg=rg.replace("i","e")
      rc=rc.replace("i","e")
      rf=rf.replace("i","e")
      rs=rs.replace("i","e")
    else:
      rg=rg.replace("u","v")
      rc=rc.replace("u","v")
      rf=rf.replace("u","v")
      rs=rs.replace("u","v")
  print(rg)
  time.sleep(2)
  os.system("clear")
  print(rc)
  time.sleep(2)
  os.system("clear")
  print(rf)
  time.sleep(2)
  os.system("clear")
  print(rs)
  if score>4:
    time.sleep(0.75)
  elif score>3:
    time.sleep(1)
  elif score>2:
    time.sleep(1.25)
  elif score>1:
    time.sleep(1.5)
  else:
    time.sleep(2)
  os.system("clear")
  answer = input("was this person a imposter?")
  if answer =="yes"and imposter==1:
    print("you are correct! they were an imposter!")
    score=score+1
  elif answer =="no" and imposter==2:
    print("correct. they are not sus.")
    score=score+1
  else:
    print("you were wrong!")
  print("next.")
  time.sleep(1)
  os.system("clear")
print("thank you for playing 'Not My Neighbor'!")
print("your final score was",score,".")
if score>4:
  print("perfect score")
  print("you earned: Detectives Badge.")
elif score>3:
  print("nice")
else:
  print("you suck!")