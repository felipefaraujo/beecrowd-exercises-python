tempo_viagem_horas = int(input())
velocidade_media_km = int(input())

qtd_litros = (tempo_viagem_horas * velocidade_media_km) / 12

print(f"{qtd_litros:.3f}")
