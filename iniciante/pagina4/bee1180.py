n = int(input())
x = list(map(int, input().split()))

menor_valor = x[0]
posicao = 0

for i in range(1, n):
    if x[i] < menor_valor:
        menor_valor = x[i]
        posicao = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao)
