
nums = [5,6,6,5]
#variable i domain starts at zero ends at 4 and has a slope of 1
biggest = nums[0]
for i in range(0,len(nums),1):
  print(nums[i])
  if nums[i] > biggest:
    biggest = nums[i]
print('biggest number is:',biggest)
list = [1,2,3,4,5]
sum = list[0]
for i in range(0,len(list),1):
  print(list[i])
  sum = sum+list[i]
print('the sum is:',sum)
nums = [1,2,3,4,5]
smallest = list[0]
for i in range(0,5,1):
  print(nums[i])
  if nums[i] < smallest:
    smallest = list[i]
print('The smallest number is:',smallest)
