a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a + b > c and a + c > b and b + c > a:
    triangulo = True
else:
    triangulo = False

if triangulo:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
