from functools import cache

def numeri_dispari(n, m = None):
    if m:
        for j in range(n, m):
            if j % 2 != 0:
                yield j
    else:
        for j in range(n):
            if j % 2 != 0:
                yield j

for k in numeri_dispari(50,70):
    print(k)

@cache
def fibonacci(j):
    if j == 0:
        return  0
    elif j == 1:
        return 1
    else:
        return   fibonacci(j-1) + fibonacci(j-2)

def fib_gen(n):
    for j in range(n):
        yield(fibonacci(j))

for k in fib_gen(50):
    print(k)