def fib(n):                                     #the function prints the first n fibonacci numbers iteratively
    n_1 = 0
    n_2 = 1
    while(n > 0):
        print(n_1)
        n_1, n_2 = n_2, n_1 + n_2
        n -= 1


print("Hello, World!")

fib(10)                                         #example of using fib(number)
