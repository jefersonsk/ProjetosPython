flag = True
dados = {}

while flag:
    try:
        codigo, nota = input().split(" ")
    except ValueError:
        print("Entrada inválida! Digite os 2 valores separados por espaço.")
        continue

    if codigo == "0" and nota == "0":
        flag = False
    else:
        try:
            nota = float(nota)
            if codigo in dados:
                dados[codigo].append(nota)
            else:
                dados[codigo] = [nota]
        except ValueError:
            print(f"A nota {nota} não é um número válido.")

for codigo, lista_dados in dados.items():
    soma_total = sum(lista_dados)
    media = soma_total / len(lista_dados)
    print(f'Código:{codigo} Média:{media}')
