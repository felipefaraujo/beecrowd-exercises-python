cod_item, quantidade_item = input().split()
cod_item = int(cod_item)
quantidade_item = int(quantidade_item)

if cod_item == 1:
    quantidade_item *= 4.00
elif cod_item == 2:
    quantidade_item *= 4.50
elif cod_item == 3:
    quantidade_item *= 5.00
elif cod_item == 4:
    quantidade_item *= 2.00
elif cod_item == 5:
    quantidade_item *= 1.50
else:
    print("Erro.")

print(f"Total: R$ {quantidade_item:.2f}")
