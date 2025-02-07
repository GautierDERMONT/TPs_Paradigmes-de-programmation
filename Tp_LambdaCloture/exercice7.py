#====Question 1====:
def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized_func

#====Question 2====:
import time

@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.time()
print("Factorielle de 20 :", factorial(20))
print("Temps d'exécution (factorielle) :", time.time() - start_time)

start_time = time.time()
print("Fibonacci de 30 :", fibonacci(30))
print("Temps d'exécution (Fibonacci) :", time.time() - start_time)