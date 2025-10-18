nums = [5,6,7,7,1,11,3,6,1,2,5,9]

hash_map = {}

for i in range(0,len(nums)):
    if nums[i] in hash_map:
        hash_map[nums[i]]+=1
    else: hash_map[nums[i]]=1

print(hash_map) 