fibonacci = []

a, b = 0, 1
while a <= (2**64 - 1):
    fibonacci.append(a)
    a, b = b, a + b

teste = int(input())

for i in range(teste):
    n = int(input())
    print(f"Fib({n}) = {fibonacci[n]}")
