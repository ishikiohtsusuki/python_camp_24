nums = [1,2,3]
biggest = nums[0]
for i in range(0,len(nums),1):
  print(nums[i])
  if nums[i] > biggest:
    biggest = nums[i]
print('biggest number is:',biggest)