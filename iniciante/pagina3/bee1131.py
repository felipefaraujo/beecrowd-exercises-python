qtd = 0
vit_inter = 0
vit_gremio = 0
empates = 0

loop = 1

while loop == 1:
    try:
        gols_inter, gols_gremio = map(int, input().split())

        qtd += 1

        if gols_gremio == gols_inter:
            empates += 1
        elif gols_gremio > gols_inter:
            vit_gremio += 1
        elif gols_inter > gols_gremio:
            vit_inter += 1

        loop = int(input("Novo grenal (1-sim 2-nao)\n"))

    except loop == 2:
        break

if vit_inter == vit_gremio:
    vencedor = "Nao houve vencedor"
elif vit_inter > vit_gremio:
    vencedor = "Inter venceu mais"
elif vit_gremio > vit_gremio:
    vencedor = "Gremio venceu mais"

print(f"{qtd} grenais")
print(f"Inter:{vit_inter}")
print(f"Gremio:{vit_gremio}")
print(f"Empates:{empates}")
print(f"{vencedor}")
