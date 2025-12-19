flag = True
gremio_ganha = 0
inter_ganha = 0
conta_jogo = 0
empates = 0

while flag:
    escolha = 0
    opcao = True

    inter, gremio = map(int, input().split(" "))
    if inter > gremio:
        inter_ganha += 1
    elif gremio > inter:
        gremio_ganha += 1
    else:
        empates += 1

    conta_jogo += 1

    while opcao:
        escolha = int(input("Novo grenal (1-sim 2-nao)\n"))

        if escolha == 1:
            opcao = False
        elif escolha ==2:
            opcao = False
            flag = False

if inter_ganha > gremio_ganha:
    resultado = "Inter venceu mais"
elif gremio_ganha > inter_ganha:
    resultado = "Gremio venceu mais"
else:
    resultado = "Nao houve vencedor"

print(f"{conta_jogo} grenais")
print(f"Inter:{inter_ganha}")
print(f"Gremio:{gremio_ganha}")
print(f"Empates:{empates}")
print(resultado)