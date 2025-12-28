arr = [5,-2,3,9,0,1,5,4,7]

n = len(arr)

temp = arr[n-1]
for i in range(n-2,-1,-1):
    arr[i+1]=arr[i]
arr[0]=temp
print(arr)

# Time Complexity: O(n)