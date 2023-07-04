while True:
    numero = int(input())

    if numero == 0:
        break

    saida = ""
    for i in range(1, numero + 1):
        saida += str(i) + " "

    print(saida[:-1])
