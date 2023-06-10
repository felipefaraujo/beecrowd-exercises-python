x, y = map(int, input().split())

contador = 0
for i in range(1, y + 1):
    contador += 1
    if contador == x:
        contador = 0
        print(i)
    else:
        print(i, end=" ")
