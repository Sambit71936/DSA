def fib(n):
    if n<=1:
        return 1
    return n+fib(n-1)

print(fib(5))


n = int(input())

a, b = 0, 1
for i in range(n+1):
    print(a)
    a, b = b, a + b