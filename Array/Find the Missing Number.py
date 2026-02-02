num = [1,0,3,4]
n= len(num)
for i in range(n):
    if i not in num:
        print(i)
        break


# Time Complexity: O(n^2)