num = int(input("Enter a number: "))
x=num
total = 0
n = len(str(num))
while x > 0:
    digit = x % 10
    total += digit ** n
    x = x // 10

if(total==num):
    print("Armstrong Number")
else: print("Not an Armstrong Numbe")