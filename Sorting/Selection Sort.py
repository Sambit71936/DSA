num = [1,2,4,7,3,98,244,53,57,8]
print(sorted(num))

def selection_sort(num):
    n = len(num)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if(num[j]<num[min]):
                min =j
        num[i],num[min]=num[min],num[i]
    return num

print(selection_sort(num))
