n = int(input())

soma = 0
for i in range(1, n + 1):
    x, y = map(int, input().split())

    for j in range(y * 2):
        if x % 2 == 0:
            x += 1
        else:
            soma += x
            print('soma =', soma)
            x += 1
    print(soma)
