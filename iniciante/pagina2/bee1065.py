valores = []
pares = 0

for i in range(5):
    valor = int(input())
    valores.append(valor)

    if valor % 2 == 0:
        pares += 1

print(f"{pares} valores pares")
