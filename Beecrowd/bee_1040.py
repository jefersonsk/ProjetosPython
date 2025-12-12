nota_01, nota_02, nota_03, nota_04 = map(float, input().split(" "))

media = ((nota_01 * 2) + (nota_02 * 3) + (nota_03 * 4) + nota_04) / 10

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    nota_final = (nota_exame + media) / 2
    if nota_final >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {nota_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nota_final:.1f}")