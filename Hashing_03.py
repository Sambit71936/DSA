#Character hashing in Python

#Constraints - 'a'<= S[i] <='z'

S = "aassddffgghhjjkkwwdncn"
l = ['d', 'a', 'w', 'k', 'n']

hash_list = []

for char in S:
    val = ord(char)
    index = val - 97
    hash_list[index] += 1
    for char in l:
        val = ord(char)
        index = val - 97
        print(hash_list[index])
