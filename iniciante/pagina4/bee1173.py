vetor = []
valor = int(input())

for i in range(10):
    vetor.append(valor)
    valor *= 2

for j in range(len(vetor)):
    print(f"N[{j}] = {vetor[j]}")
