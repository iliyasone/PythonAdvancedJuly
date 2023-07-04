import decorators

@decorators.cache_decorator
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


@decorators.time_measure_decorator
def main():
    print(f'{fib(30)=}')

if __name__ == '__main__':
    main()