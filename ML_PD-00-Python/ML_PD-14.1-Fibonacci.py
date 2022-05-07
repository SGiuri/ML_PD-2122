from functools import cache
import time

@cache
def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    r = fibonacci(n - 1) + fibonacci(n - 2)

    return r

for j in range(200):
    inizio = time.time()
    print(j, fibonacci(j), end = "\t")
    fine = time.time()
    print(fine-inizio)