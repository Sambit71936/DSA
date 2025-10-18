nums = [5,6,7,7,1,11,3,6,1,2,5,9]

dict = {}

n=len(nums)

for i in range(0,n):
    dict[nums[i]] = dict.get(nums[i],0)+1

print(dict)