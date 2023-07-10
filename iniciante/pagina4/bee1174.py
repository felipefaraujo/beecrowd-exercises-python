vetor = []
for i in range(100):
    n = float(input())
    vetor.append(n)

for j, valor in enumerate(vetor):
    if valor <= 10:
        print(f"A[{j}] = {valor}")
