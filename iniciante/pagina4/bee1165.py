teste = int(input())

soma = 0
for i in range(teste):
    n = int(input())
    for j in range(1, n + 1):
        if n % j == 0:
            soma += 1

    if soma == 2:
        print(f"{n} eh primo")
        soma = 0
    else:
        print(f"{n} nao eh primo")
        soma = 0
