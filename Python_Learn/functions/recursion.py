def fibo(n):
    if (n == 1 or n == 0):
        return n
    return fibo(n-2) + fibo(n-1)

fibo(5)

'''
how it works:

fib(5) -> fib(3)+fib(4)
fib(3) + fib(4) -> fib(1) + fib(2) + fib(2) + fib(3)
.
.
.

continues like this until the default condition is reached
    
'''