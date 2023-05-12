a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = (a + b + abs(a - b)) / 2
maior_todos = (maior + c + abs(maior - c)) / 2

print(f"{maior_todos:.0f} eh o maior")
