nums = [1,0,2,0,4,3,0,5,0]
arr = []
n = len(nums)
for i in range(n):
    if nums[i]!=0:
        arr.append(nums[i])

n2 = len(arr)
for i in range(0,n2):
    nums[i] = arr[i]

for i in range(n2,n):
    nums[i] = 0
print(nums)

# Time Complexity: O(n)