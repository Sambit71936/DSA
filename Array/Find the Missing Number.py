num = [1,0,3,4]
n= len(num)
for i in range(n):
    if i not in num:
        print(i)
        break


# Time Complexity: O(n^2)

# Using Hashing Technique
num = [1,0,3,4,7]
n= len(num)

f = {}
for i in range(n+1):
    f[i]=0

for i in num:
    f[i]=1
    
for i,j in f.items():
    if j==0:
        print(i)

# Time Complexity: O(n)