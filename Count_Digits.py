num = int(input("Enter a number: "))

count = 0
while(num > 0):
    num = num//10
    print(count)
    print(num)
    count += 1
# return count
print(count)

# or

from math import *
def count_digits(num):
    return int(log10 (num)) + 1 if num > 0 else 1

count_digits(num)