# VARIÀVEIS

lista = []
soma = 0
validar_atual = 0
contador = 0
contador_atual = 0
lista_moda = [0]

# ENTRADA DE DADOS

item_lista = int(input("Digite o nº de itens da lista: "))
print("=" * 70)

for x in range(1, item_lista + 1):
    y = float(input(f"Digite o {x}º número da lista: "))
    lista.append(y)

# Organização de forma crescente dos dados do conjunto

lista.sort()

# Cálculo Média dos valores do conjunto

for x in range(0, item_lista):
    numero = lista[x]
    soma = soma + numero

media = soma / item_lista

# Localização da Mediana 

mediana_posicao = int(item_lista / 2)

if item_lista % 2 == 0:
    posicao_01 = lista[mediana_posicao]
    posicao_02 = lista[(mediana_posicao - 1)]
    mediana = (posicao_01 + posicao_02) / 2
else:
    mediana = lista[mediana_posicao]

# Localização da Moda do conjunto

for x in range(0, item_lista):
    validar = lista[x]

    if validar != validar_atual:

        if lista.count(validar) >= contador:
            contador = lista.count(validar)

            if contador > contador_atual and validar != lista_moda[0]:
                lista_moda = []
                lista_moda.append(validar)
            elif contador == contador_atual:
                lista_moda.append(validar)
            validar_atual = validar
            contador_atual = contador

# SAÍDA DE DADOS

print("=" * 70)
print(f'CONJUNTO ORDENADO: {lista}')
print(f'MODA: {lista_moda} - {contador} vezes')
print(f'MÉDIA: {media:.2f}')
print(f'MEDIANA: {mediana:.2f}')