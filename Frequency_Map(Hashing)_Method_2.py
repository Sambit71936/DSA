nums = [5,6,7,7,1,11,3,6,1,2,5,9]

hash_map = {}

n=len(nums)

for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1

print(hash_map)