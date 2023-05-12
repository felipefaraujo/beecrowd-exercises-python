vendedor = input()
salario_fixo = float(input())
vendas_mes = float(input())

salario = (vendas_mes * 0.15) + salario_fixo

print(f"TOTAL = R$ {salario:.2f}")
