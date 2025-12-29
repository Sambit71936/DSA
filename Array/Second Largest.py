arr = list(map(int,input().split()))

first = second = float('-inf')

for i in range(0,len(arr)):
    if arr[i]>first:
        first = arr[i]
    for i in range(0,len(arr)):
        if arr[i]>second and arr[i]<first:
            second = arr[i]
print(second)

# Time Complexity: O(n)    