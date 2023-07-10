vetor = []
for i in range(10):
    n = int(input())

    if n <= 0:
        n = 1
        vetor.append(n)
    else:
        vetor.append(n)

for j in range(len(vetor)):
    print(f"X[{j}] = {vetor[j]}")
