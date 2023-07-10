vetor = []
valor = float(input())

contador = 0
while True:
    vetor.append(valor)
    while contador < 99:
        contador += 1
        valor /= 2.0
        vetor.append(valor)
    break

for x, y in enumerate(vetor):
    print(f"N[{x}] = {y:.4f}")
