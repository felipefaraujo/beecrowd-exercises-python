valores = input().split()
A = int(valores[0])
ultimo_valor = len(valores) - 1
N = int(valores[ultimo_valor])

while N <= 0:
    N = int(input())

soma = 0
for i in range(0, N):
    soma += A + i

print(soma)
