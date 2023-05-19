valor = int(input())
impar = 1

for i in range(valor):
    print(impar)
    impar += 2
    if impar > valor:
        break
