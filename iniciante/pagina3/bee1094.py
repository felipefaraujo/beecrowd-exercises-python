valor = int(input())
soma = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(1, valor + 1):
    quantia, tipo = input().split()
    quantia = int(quantia)

    soma += quantia

    if tipo == "C":
        coelhos += quantia
    elif tipo == "R":
        ratos += quantia
    elif tipo == "S":
        sapos += quantia

percentual_coelhos = 100 / (soma / coelhos)
percentual_ratos = 100 / (soma / ratos)
percentual_sapos = 100 / (soma / sapos)

print(f"Total: {soma} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
