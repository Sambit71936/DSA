# Parameterized Recursion Example

def func(sum,i,n):
    if i > n:
        return
    sum += i
    print(sum)
    func(sum, i + 1, n)

func(0,1,4)

# Functional Recursion

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))