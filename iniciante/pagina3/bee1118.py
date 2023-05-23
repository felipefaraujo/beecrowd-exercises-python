while True:
    media = 0.0
    contador = 0

    while contador < 2:
        nota = float(input())
        if nota < 0.0 or nota > 10.0:
            print("nota invalida")
        else:
            media += nota
            contador += 1

    media_final = media / 2.0
    print(f"media = {media_final:.2f}")

    opcao = 0
    while opcao != 1 and opcao != 2:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())

    if opcao == 2:
        break
