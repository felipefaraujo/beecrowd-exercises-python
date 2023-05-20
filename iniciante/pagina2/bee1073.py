valor = int(input())
base = 1

for i in range(1, valor + 1):
    if base % 2 == 0:
        print(f"{base}^2 = {base**2}")
        base += 1
    else:
        base += 1
