def time_it(original_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        my_exec = original_func(*args, **kwargs)
        delta_t = time.time() - t1
        print(f"Delta_t = {delta_t}")
        return my_exec
    return wrapper

def my_decorator(original_function):
    def wrapper(*args, **kwargs):
        print("Execued before")
        my_func = original_function(*args, **kwargs)
        print("Executed after")
        return my_func
    return wrapper

@time_it
def test_func(a,b, c =9):
    import time
    time.sleep(5)
    print(a, b, c, a+b)
    return a + b

# test_func(5,6)

# time_it(test_func(5,6))

def div_zero_check(original_function):
    def wrapper(a,b):
        if b == 0:
            print("Zero division")
            return "-"
        else:
            my_func = original_function(a, b)
            return my_func
    return wrapper

@div_zero_check
def divisione(a, b):
    return a / b

print(divisione(5,3))
print(divisione(5,0))