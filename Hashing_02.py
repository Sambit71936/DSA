n = [1,3,5,3,6,7,2,9,10,4,7,9,8]
m = [7,2,8,3,4,2,11,4,5,1,3,1,9,8,7]

#using dictionary
hash_map = {}

for num in n:
    hash_map[num] += 1
    for num in m:
        if num in hash_map:
            print(hash_map[num])
        else:
            print(0)
   
