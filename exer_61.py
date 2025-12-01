conta_doadores = 0
conta_nao_doadores = 0
x = 1
idade_valida = peso_valido = jejum_valido = False

while x <= 3:
    try: 
        print(f'Doador {x}')
        print(8 * "=")

        if idade_valida == False:
            idade = int(input('Idade: '))
            if idade <= 0:
                raise ValueError("Erro 1: Valor digitado é negativo.")
            else:
                idade_valida = True
        else:
            print(f'Idade: {idade}')

        if peso_valido == False:
            peso = float(input('Peso: '))
            if peso <= 0:
                raise ValueError("Erro 1: Valor digitado é negativo.")
            else:
                peso_valido = True
        else:
            print(f'Peso: {peso}')

        if jejum_valido == False:
            jejum = input('Jejum [S] ou [N]: ').upper()
            if jejum not in "SN":
                raise ValueError("Erro 3: Valor digitado está incorreto. Digite somente S ou N.")
            else:
                jejum_valido = True

        if idade_valida and peso_valido and jejum_valido:

            if (18 <= idade <= 67) and (peso >= 50) and (jejum == "S"):
                conta_doadores += 1
            else:
                conta_nao_doadores += 1
            x = x + 1
            idade_valida = peso_valido = jejum_valido = False

            print()

    except Exception as e:
        print(e)
        print()

print(f'Doadores: {conta_doadores}')
print(f'Não Doadores: {conta_nao_doadores}')