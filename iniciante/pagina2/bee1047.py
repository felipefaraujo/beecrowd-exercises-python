hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

total_inicial = hora_inicial * 60 + minuto_inicial
total_final = hora_final * 60 + minuto_final

tempo = total_final - total_inicial

if tempo <= 0:
    tempo = tempo + 24 * 60

horas = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
