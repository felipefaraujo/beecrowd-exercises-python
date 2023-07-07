idades = []
while True:
    n = int(input())
    if n <= 0:
        break
    else:
        idades.append(n)

soma = 0
for i in idades:
    soma += i

media = soma / len(idades)

print(f"{media:.2f}")
