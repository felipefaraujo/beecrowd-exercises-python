qtd = int(input())

for i in range(qtd):
    numero1, numero2 = map(int, input().split())
    inicio = min(numero1, numero2) + 1
    fim = max(numero1, numero2)
    soma_impares = 0
    if numero1 == numero2 or numero2 == numero1:
        print(soma_impares)
    else:
        for numero in range(inicio, fim):
            if numero % 2 != 0:
                soma_impares += numero

        print(soma_impares)
