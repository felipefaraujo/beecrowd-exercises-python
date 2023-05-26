alcool = 0
gasolina = 0
diesel = 0
gas = 0

while True:
    gas = int(input())
    if gas == 1:
        alcool += 1
    elif gas == 2:
        gasolina += 1
    elif gas == 3:
        diesel += 1
    elif gas == 4:
        break
    if gas > 4 or gas < 1:
        continue

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
