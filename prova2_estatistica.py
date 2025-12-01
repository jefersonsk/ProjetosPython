from funcoes import calcula_media
from funcoes import calcula_desviopadrao
from funcoes import calcula_desviomedio
from funcoes import calcula_mediana
from funcoes import localiza_moda

dados = []

quantidade_dados = int(input("Digite o nº de itens da lista: "))
print("=" * 70)

for x in range(0, quantidade_dados):
    y = float(input(f"Digite o {x + 1}º número da lista: "))
    dados.append(y)

dados.sort()

media = calcula_media(dados)
desvio_padrao = calcula_desviopadrao(dados, media)
desvio_medio = calcula_desviomedio(dados, media)
coeficiente_variacao = (desvio_padrao / media) * 100
mediana = calcula_mediana(dados)
moda = localiza_moda(dados, quantidade_dados)

print(f"DADOS: {dados}")
print(f"MÉDIA: {media:.2f}")
print(f"MODA: {moda}")
print(f"MEDIANA: {mediana}")
print(f"DESVIO PADRÃO: {desvio_padrao:.2f}")
print(f"DESVIO MÉDIO: {desvio_medio:.2f}")
print(f"COEFICENTE DE VARIAÇÃO: {coeficiente_variacao:.2f}%")