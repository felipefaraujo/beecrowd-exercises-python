valores = []
pares = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    valor = int(input())
    valores.append(valor)

    if valor % 2 == 0:
        pares += 1

    if valor % 2 != 0:
        impar += 1

    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1

print(f"{pares} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
