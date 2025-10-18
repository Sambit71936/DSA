n = [1,3,5,3,6,7,2,9,10,4,7,9,8]
m = [7,2,8,3,4,2,11,4,5,1,3,1,9,8,7]



#for i in range(0,n):
#    count= 0
#    for j in range(0,m):
#        if m[i]==n[j]:
#            count+=1
#    print(f'the element {a[i]} occurs {count} in b')
#
#
#for i in a:
#    count = 0
#    for j in b:
#        if i == j:
#            count+=1 
#print(count)

hash_list = [0]*11

for num in n:
    hash_list[num]+=1
    for num in m:
        if num<1 or num>10:
            print(0)
        else:
            print(hash_list[num])

#T(complexity): O(n + m)