vetor = []
valor = int(input())

contador = 0
i = 0
while True:
    vetor.append(i)
    i += 1
    contador += 1
    if i == valor:
        i = 0

    if contador == 1000:
        break

for j, v in enumerate(vetor):
    print(f"N[{j}] = {v}")
