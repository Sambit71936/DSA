arr = [23, 12, 45, 67, 34, 89, 10]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


print(bubble_sort(arr))

# Time Complexity: O(n^2)
