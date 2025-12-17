# Using if-else

s = input("Enter a string: ")

a = s[::-1]

if s==a:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Using While Loop

n = len(s)
left = 0
right = n-1

while(left<right):
    if s[left]!=s[right]:
        print("Not a Palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")

# Using Recursion   