n = int(input("Enter the number: "))

a=0
b=1
if n<=0:
    print(n)
for i in range(n+1):
    print(a)
    temp =a
    a=b
    b=temp+b