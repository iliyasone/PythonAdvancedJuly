from decorators import cache_decorator


@cache_decorator
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


@decorators.time_measure_decorator
def main():
    fib(50)
    
    print(fib.cache)

#@decorators.cache_decorator
def compute_square(x):
    print("computing....")
    return x*x


if __name__ == '__main__':
    main()