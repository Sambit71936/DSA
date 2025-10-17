num = int(input("Enter a number: "))
result = 0

while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10
print(result)
