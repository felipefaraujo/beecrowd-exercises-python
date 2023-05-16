salario = float(input())

if 0.00 <= salario <= 2000.00:
    print("Isento")
elif 2000.01 <= salario <= 3000.00:
    imposto = (salario - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif 3000.01 <= salario <= 4500.00:
    imposto = ((salario - 3000.00) * 0.18) + 80.00
    print(f"R$ {imposto:.2f}")
elif salario > 4500.00:
    imposto = ((salario - 4500.00) * 0.28) + 80.00 + 270.00
    print(f"R$ {imposto:.2f}")
