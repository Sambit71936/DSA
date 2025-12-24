# Merge two sorted arrays

left = [1,2,3,4]
right =[1,1,3,4,5,6,7]

def merge_array(left,right):
    merge=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            merge.append(left[i])
            i+=1
        else:
            merge.append(right[j])
            j+=1
    if i<n:
        while i<n:
            merge.append(left[i])
            i+=1
    
    if j<m:
        while j<m:
            merge.append(right[j])
            j+=1
    return merge

print(merge_array(left,right))

# Merge Sort

arr=[3,1,4,7,5,9,8,2,6]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)

print(merge_sort(arr))


# Time Complexity: O(n log n)