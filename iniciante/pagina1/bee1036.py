import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a > 0 and b > 0 and 0 < c < b:
    x1 = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
else:
    print("Impossivel calcular")

