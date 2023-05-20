casos = int(input())

for i in range(casos):
    x, y, z = map(float, input().split())
    media = ((x * 2.0) + (y * 3.0) + (z * 5.0)) / (2.0 + 3.0 + 5.0)
    print(f"{media:.1f}")
