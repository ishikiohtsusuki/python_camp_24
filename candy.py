import random
import time
import os
candy = 0
wonka=random.randint(1,100)
for i in range(100):
  dice = random.randint(1,4)
  if wonka==1:
    break
  if dice==1:
    candy=candy+random.randint(1,4)
    print("you got candies!")
    print("you have",candy,"candies!")
  elif dice==2:
    print("you got a toothbrush!")
  else:
    print("you dident get any candy.")
  dice2=random.randint(1,10)  
  if candy>3:
    if dice2 == 1:
      candy=candy-random.randint(1,3)
      print("someone stole your candy!")
    
  time.sleep(0.5)
  os.system("clear")
if wonka == 1:
  print("you got a golden ticket!")
  wc=input("would you like to keep the candy or give it to a friend? enter keep to keep if or anything else to give it away.")
  if wc=="keep":
    print("you havde infinite candy!")
  else:
    print("your friend has infinite candy and dosent give you any!")
  if wc == "keep":
    print("you have infinite candy!")
    
print("its late and you finished trick or treating!\n")
print("you got",candy,"candies from your trick or treating.")