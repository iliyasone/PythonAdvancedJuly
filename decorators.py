import time

def time_measure_decorator(func): 
    def wrapper(*params, **kwargs):
        start_time = time.time()
        
        result = func(*params, **kwargs)
        
        end_time = time.time()
        print(f'{func.__name__}{params} was runnig for {end_time-start_time}')
        
        return result
    return wrapper

def cache_decorator(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        cache[args] = func(*args)
        
        return cache[args]
    wrapper.cache = cache
    
    return wrapper

@time_measure_decorator
def hard_computation_function(n):
    time.sleep(n)
    print('function done!')


def main():
    hard_computation_function(2)
    

if __name__ == '__main__':
    main()

    