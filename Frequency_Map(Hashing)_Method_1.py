nums = [5,6,7,7,1,11,3,6,1,2,5,9]

dict = {}

for i in range(0,len(nums)):
    if nums[i] in dict:
        dict[nums[i]]+=1
    else: dict[nums[i]]=1

print(dict) 