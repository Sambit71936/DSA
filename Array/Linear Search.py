nums = [5,3,9,1,6,2,8,4,7,9]

target = int(input())

for i in range(len(nums)):
    if nums[i]==target:
        print(i)
    else:
        print(-1)


# Time Complexity: O(n)