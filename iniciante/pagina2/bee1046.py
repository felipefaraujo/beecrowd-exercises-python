hora_inicial, hora_final = map(int, input().split())

hora_inicial *= 3600
hora_final *= 3600

if hora_inicial >= hora_final:
    tempo = ((86400 - hora_inicial) + hora_final) // 3600
    print(f"O JOGO DUROU {tempo} HORA(S)")
else:
    tempo = abs(hora_inicial - hora_final) // 3600
    print(f"O JOGO DUROU {tempo} HORA(S)")
