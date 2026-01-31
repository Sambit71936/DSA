arr1 = [1,2,3,4,5]
arr2 = [3,4]

n,m = len(arr1), len(arr2)

for i in range(n):
    for j in range(m):
        if arr1[i]==arr2[j]:
            print(arr1[i])
            break


        