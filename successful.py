# import random
# colers = ['red','green','blue']
# shapes = ['triangle','square','pentagon']
# num = random.randint (0,2)
# # print(colers[num],shapes[num])
import random
items=['1.raisens','2.water','3.soda','4.orange juice','5.chocolate bar','6.stuffed animal','7.knuckle sandwich']
prices=[4,6,8,11,23,12,100]
wallet = random.randint (69,169)
print("wallet:", wallet)
for i in range(len(items)):
  print(items[i],"$",str(prices[i]))
while True:
  item=input("Choose an itemn you would like to purchase. (s to purchase)")
  if item == "s":
    break
  wallet = wallet - prices[int(item)-1]
print("wallet:",wallet)
if wallet>0:
  print("Your remaining balance is:", wallet)
else:
  print("You went bankrupt. HaHaHa!!")