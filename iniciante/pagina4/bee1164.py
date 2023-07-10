teste = int(input())

soma = 0
for i in range(teste):
    n = int(input())
    for j in range(1, n + 1):
        if j == n:
            continue
        elif n % j == 0:
            soma += j

    if soma == n:
        print(f"{n} eh perfeito")
        soma = 0
    else:
        print(f"{n} nao eh perfeito")
        soma = 0
