tempo_segundos = int(input())

hora = tempo_segundos // 3600
tempo_segundos %= 3600
minutos = tempo_segundos // 60
tempo_segundos %= 60
segundos = tempo_segundos

print(f"{hora}:{minutos}:{segundos}")
