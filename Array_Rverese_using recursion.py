# n= int(input("Enter the size of array: "))
# arr= []
# for i in range(n):
#     e= int(input("Enter the element: "))
#     arr.append(e)

# print(arr)
arr = [1,13,15,23,14,56]
left = 0
right = len(arr)-1

def func(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    func(arr,left+1,right-1)

func(arr,1,4)
func(arr,left,right)
print(arr)

