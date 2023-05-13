n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2.0 + n2 * 3.0 + n3 * 4.0 + n4 * 1.0) / 10.0
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2.0
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado.")

