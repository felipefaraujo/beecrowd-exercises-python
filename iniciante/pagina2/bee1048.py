salario = float(input())

if 0 <= salario <= 400.00:
    novo_salario = salario * 1.15
    reajuste = novo_salario - salario
    porcentagem = 15
elif 400.01 <= salario <= 800.00:
    novo_salario = salario * 1.12
    reajuste = novo_salario - salario
    porcentagem = 12
elif 800.01 <= salario <= 1200.00:
    novo_salario = salario * 1.1
    reajuste = novo_salario - salario
    porcentagem = 10
elif 1200.01 <= salario <= 2000.00:
    novo_salario = salario * 1.07
    reajuste = novo_salario - salario
    porcentagem = 7
else:
    novo_salario = salario * 1.04
    reajuste = novo_salario - salario
    porcentagem = 4

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {porcentagem:.0f} %")
