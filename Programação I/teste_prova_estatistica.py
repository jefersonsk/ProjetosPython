from funcoes import calcula_mediana
from funcoes import calcula_media
from funcoes import calcula_variancia
from funcoes import calcula_desviomedio
from funcoes import calcula_mediana
from funcoes import localiza_moda

lista = []
temp = []
xi = []
fi = []
xi_fi = []
xi2_fi = []
soma_fi = 0
soma_xifi = 0
soma_xi2fi = 0
acumulada = 0
frequencia_acumulada = []
desvio = 0

distribuicao = input("Com distribuição (S) ou (N): ")

if distribuicao.upper() == "S":
    tipo = input("Intervalo de Classe (S) ou (N): ")

quantidade = int(input("Digite a quantidade de dados: "))

if distribuicao.upper() == "S":
    for x in range(0, quantidade):
        if tipo.upper() == "N":
            lista.append(input(f"Digite {x + 1}º conjunto de dados (xi) (fi): ").split(" "))
        else:
            inicio_int, termina_int, fi_aux = input(f"Digite {x + 1}º conjunto de dados ([) ([) (fi): ").split(" ")
            calculo_xi = (int(inicio_int) + int(termina_int)) / 2
            lista.append([calculo_xi, int(fi_aux)])

        xi_fi.append(int(lista[x][0]) * int(lista[x][1]))
        xi2_fi.append(int(lista[x][0])**2 * int(lista[x][1]))
        soma_fi = soma_fi + int(lista[x][1])
        xi.append(int(lista[x][0]))
        fi.append(int(lista[x][1]))
        acumulada = acumulada + int(lista[x][1])
        frequencia_acumulada.append(acumulada)

    soma_xifi = sum(xi_fi)
    soma_xi2fi = sum(xi2_fi)
    media = soma_xifi / soma_fi
    variancia = (1/soma_fi) * (soma_xi2fi - ((soma_xifi**2) / soma_fi))
    moda = max(fi)
    
    for x in range(0, quantidade):
        desvio = desvio + (abs(xi[x] - media) * fi[x])
    desvio_medio = desvio / sum(fi)

    if tipo.upper() == "N":
        calculo_mediana = (sum(fi) + 1) / 2
        mediana = calcula_mediana(xi)
    else:
        calculo_mediana = sum(fi) / 2
        mediana = 0
else:
    for x in range(0, quantidade):
        y = float(input(f"Digite o {x + 1}º número da lista: "))
        lista.append(y)

    lista.sort()

    media = calcula_media(lista)
    variancia = calcula_variancia(lista, media)
    mediana = calcula_mediana(lista)
    moda = localiza_moda(lista, quantidade)
    desvio_medio = calcula_desviomedio(lista, media)

desvio_padrao = variancia**0.5
coeficiente_variacao = (desvio_padrao / media) * 100

print(60 * "=")
if distribuicao.upper() == "S":
    print(f"xi: {xi}    SOMA: {sum(xi)}")
    print(f"fi: {fi}    SOMA: {sum(fi)}")
    print(f"Fi: {frequencia_acumulada}")
    print(f"xi*fi: {xi_fi}   SOMA: {sum(xi_fi)}")
    print(f"(xi^2)*fi: {xi2_fi}   SOMA: {sum(xi2_fi)}")
    print(f"CÁLCULO MEDIANA: {calculo_mediana:.2f}")
    
print(f"MODA: {moda}")
print(f"MEDIANA: {mediana}")
print(f"DESVIO MÉDIO: {desvio_medio:.2f}")
print(f"VARIÂNCIA: {variancia:.2f}")
print(f"MÉDIA: {media:.2f}")
print(f"DESVIO PADRÃO: {desvio_padrao:.2f}")
print(f"COEFICIENTE DE VARIAÇÃO: {coeficiente_variacao:.2f}%")