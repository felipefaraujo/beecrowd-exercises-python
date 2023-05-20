valores = []
contador = int(input())

for i in range(contador):
    valor = int(input())
    valores.append(valor)

    if valor % 2 == 0 and valor > 0:
        print("EVEN POSITIVE")
    elif valor % 2 == 0 and valor < 0:
        print("EVEN NEGATIVE")
    elif valor % 2 != 0 and valor > 0:
        print("ODD POSITIVE")
    elif valor % 2 != 0 and valor < 0:
        print("ODD NEGATIVE")
    elif valor == 0:
        print("NULL")
