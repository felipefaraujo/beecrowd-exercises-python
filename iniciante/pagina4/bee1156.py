soma = 0
j = 2
for i in range(3, 39, 2):
    divisao = i / j
    j *= 2
    soma += divisao

soma = soma + 1
print(f"{soma:.2f}")
