soma = 0
for i in range(2, 101):
    divisao = 1 / i
    soma += divisao

soma = soma + 1
print(f"{soma:.2f}")
