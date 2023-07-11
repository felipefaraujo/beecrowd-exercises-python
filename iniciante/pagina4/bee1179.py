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

for valor in vetor:
    if valor % 2 == 0:
        if contador_par >= 5:
            par2.append(valor)
        else:
            contador_par += 1
            par.append(valor)
    elif valor % 2 != 0:
        if contador_impar >= 5:
            impar2.append(valor)
        else:
            contador_impar += 1
            impar.append(valor)

for j, v in enumerate(par):
    print(f"par[{j}] = {v}")

for k, v in enumerate(impar):
    print(f"impar[{k}] = {v}")

for l, v in enumerate(impar):
    print(f"impar[{l}] = {v}")

for m, v in enumerate(par):
    print(f"par[{m}] = {v}")
