qtd = int(input())

for i in range(qtd):
    x, y = map(int, input().split())

    if y == 0:
        print("divisao impossivel")
    elif x == 0:
        divisao = 0.0
        print(divisao)
    else:
        divisao = x / y
        print(divisao)
