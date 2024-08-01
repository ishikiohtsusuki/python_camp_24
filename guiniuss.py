# import random
# color = ["red","yellow","blue"]
# shape = ["square","triangle","pentagon"]
# r1 = random.choice(color)
# r2 = random.choice(shape)
# print(r1+" "+r2)
# r3=random.randint(0,2)
# for i in range(1):
#   if r3==0:
#     print(shape[0]+" "+color[0])
#   elif r3 == 1:
#     print(shape[1]+" "+color[1])
#   else:
#     print(shape[2]+ " "+color[2])
import random
import os
import time

wallet = random.randint(100, 200)
store = [
    "1. water", "2. dragon", "3. meal", "4. soda", "5. chocolate",
    "6. lemonade", "7. labtop", "8. lightbulb"
]
prices = [23, 55, 13, 6, 9, 4, 69, 32]
for g in range(len(prices)):
  price = random.randint(0, 69)
  proo = random.choice(prices)
  prices.remove(proo)
  prices.append(price)

print("you have", wallet, "dollars.")
print("In stock:")
for i in range(len(store)):
  print(store[i] + " $" + str(prices[i]))
while True:
  cart = int(
      input(
          "enter the number of the product which you would like to buy or 10 to proceed to checkout."
      )) - 1
  if cart == 9:
    break

  for j in range(len(store)):
    if cart == j:
      print("you have purchased #", store[j])
      wallet = wallet - prices[j]
      break
if wallet > 100:
  print("The stock market crashed!")
elif wallet > 0:
  print(" you have sucsesfully bought stuff!")
  print("your remaining wallet balance is", wallet, "dollars.")
else:
  print("you went over budget!")
  print("you spent", wallet * -1, "too many dollars!")
