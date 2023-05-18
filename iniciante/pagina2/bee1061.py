dia1 = int(input().split()[1])
hora1, min1, seg1 = map(int, input().split(":"))
tempo1 = seg1 + min1 * 60 + hora1 * 3600 + dia1 * 86400

dia2 = int(input().split()[1])
hora2, min2, seg2 = map(int, input().split(":"))
tempo2 = seg2 + min2 * 60 + hora2 * 3600 + dia2 * 86400

dif = tempo2 - tempo1

d = dif // 86400
dif %= 86400

h = dif // 3600
dif %= 3600

m = dif // 60
s = dif % 60

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")
