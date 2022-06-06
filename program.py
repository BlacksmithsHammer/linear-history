def fib(n):                                     #a function that returns the fibonacci number in a series with (0, 1, 1, 2, 3, 5...)
    if n > 3: return fib(n - 1) + fib(n - 2)
    if n > 1: return 1
    return 0

print("Hello, World!")

print(fib(10))                                  #example of using fib(number)
