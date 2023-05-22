while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    start = min(m, n)
    end = max(m, n)

    sequencia = ''
    soma = 0

    for i in range(start, end + 1):
        sequencia += str(i) + ' '
        soma += i

    print(f"{sequencia.strip()} Sum={soma}")
