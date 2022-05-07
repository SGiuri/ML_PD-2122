
def my_generator(n):
    for j in range(n):
        if j % 2 == 0:
            yield j
            
# print(my_generator(10))

# for my_num in my_generator(100):
#     print(my_num)

#
# print(my_generator(100).next())

my_list_gen = [n for n in range(100) if n % 2 == 0]
print(my_list_gen)

y_gen = (n for n in range(100) if n % 2 == 0)
print(y_gen)
print(y_gen)


def my_new_gen():
    yield 1
    yield 2
    yield 3

my_g = my_new_gen()

for j in my_g:
    print(j)



# from functools import cache
# 
# def numeri_dispari(n, m = None):
#     if m:
#         for j in range(n, m):
#             if j % 2 != 0:
#                 yield j
#     else:
#         for j in range(n):
#             if j % 2 != 0:
#                 yield j
# 
# for k in numeri_dispari(50,70):
#     print(k)
# 
# @cache
# def fibonacci(j):
#     if j == 0:
#         return  0
#     elif j == 1:
#         return 1
#     else:
#         return   fibonacci(j-1) + fibonacci(j-2)
# 
# def fib_gen(n):
#     for j in range(n):
#         yield(fibonacci(j))
# 
# for k in fib_gen(50):
#     print(k)