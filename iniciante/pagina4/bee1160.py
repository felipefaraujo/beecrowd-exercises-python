teste = int(input())

for i in range(teste):
    pa, pb, g1, g2 = map(str, input().split())
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    contador = 0
    while pa <= pb:
        pa = pa + (pa * (g1 / 100))
        pb = pb + (pb * (g2 / 100))
        contador += 1

    if contador > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{contador} anos.")
