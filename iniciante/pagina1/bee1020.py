idade_dias = int(input())

ano = idade_dias // 365
idade_dias %= 365

mes = idade_dias // 30
idade_dias %= 30

dia = idade_dias

print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")
