arr = list(map(int,input("Enter the elements of the array separated by space: ").split()))
print(arr)

largest = arr[0]
for i in range(0,len(arr)):
    if arr[i]>largest:
        largest = arr[i]
print(largest)

#time Complexity: O(n)