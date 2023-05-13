valor = float(input())

cem = valor // 100.0
valor %= 100.0

cinq = valor // 50.0
valor %= 50.0

vinte = valor // 20.0
valor %= 20.0

dez = valor // 10.0
valor %= 10.0

cinco = valor // 5.0
valor %= 5.0

dois = valor // 2.0
valor %= 2.0

um = valor // 1.0
valor %= 1.0

cinq_centavos = (valor * 10) // 5.0
valor = (valor * 10) % 5.0

vinte_centavos = (valor / 10) // 0.25
valor = (valor / 10) % 0.25

dez_centavos = (valor * 10) // 1.0
valor = (valor * 10) % 1.0

cinco_centavos = (valor / 10) // 0.05
valor = (valor / 10) % 0.05

um_centavo = valor // 0.01

print("NOTAS:")
print(f"{cem:.0f} nota(s) de R$ 100.00")
print(f"{cinq:.0f} nota(s) de R$ 50.00")
print(f"{vinte:.0f} nota(s) de R$ 20.00")
print(f"{dez:.0f} nota(s) de R$ 10.00")
print(f"{cinco:.0f} nota(s) de R$ 5.00")
print(f"{dois:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{um:.0f} moeda(s) de R$ 1.00")
print(f"{cinq_centavos:.0f} moeda(s) de R$ 0.50")
print(f"{vinte_centavos:.0f} moeda(s) de R$ 0.25")
print(f"{dez_centavos:.0f} moeda(s) de R$ 0.10")
print(f"{cinco_centavos:.0f} moeda(s) de R$ 0.05")
print(f"{um_centavo:.0f} moeda(s) de R$ 0.01")
