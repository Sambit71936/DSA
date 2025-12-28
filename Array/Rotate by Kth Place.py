nums = [3,9,5,6,7,8,1,2,4]

k = int(input())
n=len(nums)

rotation = k%n

for _ in range(0, rotation):
    e = nums.pop()
    nums.insert(0, e)
print(nums)
