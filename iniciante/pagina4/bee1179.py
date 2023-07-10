vetor = []
par = []
impar = []
par2 = []
impar2 = []

for i in range(15):
    n = int(input())
    vetor.append(n)

contador_par = 0
contador_impar = 0

for j, valor in enumerate(vetor):
    if valor % 2 == 0 and contador_par < 5:
        par.append(valor)
        contador_par += 1
    elif valor % 2 == 0 and contador_par >= 5:
        par2.append(valor)
    elif valor % 2 != 0 and contador_impar < 5:
        impar.append(valor)
        contador_impar += 1
    elif valor % 2 != 0 and contador_impar >= 5:
        impar2.append(valor)

for x, valor in enumerate(par):
    print(f"par[{x}] = {valor}")

for w, valor in enumerate(impar):
    print(f"impar[{w}] = {valor}")

for z, valor in enumerate(impar2):
    print(f"impar[{z}] = {valor}")

for y, valor in enumerate(par2):
    print(f"par[{y}] = {valor}")
