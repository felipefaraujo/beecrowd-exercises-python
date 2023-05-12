cod1, num1, valor1 = input().split()
cod2, num2, valor2 = input().split()

cod1 = int(cod1)
cod2 = int(cod2)

total = int(num1) * float(valor1) + int(num2) * float(valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
