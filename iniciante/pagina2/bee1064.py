valores = []
positivos = 0
soma = 0

for i in range(6):
    valor = float(input())
    valores.append(valor)

    if valor > 0:
        positivos += 1
        soma += valor

media = soma / positivos
print(f"{positivos} valores positivos")
print(f"{media:.1f}")
