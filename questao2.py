def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return f'O numero {n} pertence a sequencia de Fibonacci'
    else:
        return f'O numero {n} não pertence a sequencia de Fibonacci'
    
print(fibonacci(13))