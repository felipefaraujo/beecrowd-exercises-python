A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B, C = C, B

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or A == C != B or B == C != A:
        print("TRIANGULO ISOSCELES")
