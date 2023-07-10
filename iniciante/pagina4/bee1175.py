vetor = []

for i in range(20):
    n = input()
    vetor.append(n)
copy = tuple(vetor)

cont = -1
for j, valor in enumerate(vetor):
    vetor[j] = copy[cont]
    cont -= 1

for k, valor in enumerate(vetor):
    print(f"N[{k}] = {valor}")
