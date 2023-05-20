valores = []
contador = int(input())
dentro = 0
fora = 0

for i in range(contador):
    valor = int(input())
    valores.append(valor)

    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in\n{fora} out")
