def ntimes(n):
    def inner(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                rv = fn(args, kwargs)
            # return rv
        return wrapper
    return inner

@ntimes(2)
def print_num(*nums, **kwargs):
    print(nums)

 print_num(1, car='bmw')

