arr = [1,1,2,3,4,4,5,6,6,6,7,7,8,8,8,8,9,9,9,9]

def remove_duplicates(arr):
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    return unique_arr

print(remove_duplicates(arr))

# Time Complexity: O(n^2)