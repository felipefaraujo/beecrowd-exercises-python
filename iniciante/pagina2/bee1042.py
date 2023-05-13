x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x > y and x > z:
    maior = x
    if y > z:
        meio = y
        fim = z
    else:
        meio = z
        fim = y
elif y > x and y > z:
    maior = y
    if x > z:
        meio = x
        fim = z
    else:
        meio = z
        fim = x
else:
    maior = z
    if x > y:
        meio = x
        fim = y
    else:
        meio = y
        fim = x

print(f"{fim}\n{meio}\n{maior}")
print()
print(f"{x}\n{y}\n{z}")
