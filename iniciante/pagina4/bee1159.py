soma = 0
while True:
    x = int(input())

    if x == 0:
        break

    if x % 2 != 0:
        x += 1

    for i in range(1, 6):
        soma += x
        x += 2

    print(soma)
    if soma != 0:
        soma = 0
