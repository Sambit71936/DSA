arr = [23, 12, 45, 67, 34, 89, 10]
def is_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

print(is_sorted(arr))

# Time Complexity: O(n)