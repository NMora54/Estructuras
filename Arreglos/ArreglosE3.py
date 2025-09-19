def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
n = int(input("Ingrese la cantidad de dígitos de la serie de Fibonacci que desea: "))
print(fibonacci(n))
