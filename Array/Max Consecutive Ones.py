def max_con(nums):
    mc = 0
    c = 0
    for i in range(0,len(nums)):
        if nums[i]==1:
            c +=1
        else:
            mc = max(mc,c)
            c = 0
    return max(mc,c)


nums = [1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1]

print(max_con(nums))