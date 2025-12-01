def verifica_primo(valor: int) -> str:
    contador = 1
    for x in range(1, valor):
        calculo = valor % x
        if calculo == 0:
            contador +=1

    if contador == 2:
        primo = True
    else:
        primo = False

    return primo

# FUNÇÃO MÉDIA

def calcula_media(valor) -> float:
    soma = 0

    for x in valor:
        soma = soma + x

    media = soma / len(valor)

    return media

# FUNÇÃO DESVIO PADRÃO

def calcula_variancia(valor: list, media: float) -> float:
    diferenca = 0
    quadrado = 0
    soma_quadrado = 0

    for y in valor:
        diferenca = y - media
        quadrado = diferenca ** 2
        soma_quadrado = soma_quadrado + quadrado

    variancia = soma_quadrado / (len(valor) - 1)
 
    return variancia

# FUNÇÃO DESVIO MÉDIO

def calcula_desviomedio(valor: list, media: float) -> float:
    diferenca = 0
    soma_valores = 0

    for x in valor:
        diferenca = x - media
        soma_valores = soma_valores + abs(diferenca)

    desvio_medio = soma_valores / len(valor)

    return desvio_medio

# FUNÇÃO MEDIANA

def calcula_mediana(valor: list) -> float:
    mediana_posicao = int(len(valor) / 2)

    if len(valor) % 2 == 0:
        posicao_01 = valor[mediana_posicao]
        posicao_02 = valor[(mediana_posicao - 1)]
        mediana = (posicao_01 + posicao_02) / 2
    else:
        mediana = valor[mediana_posicao]

    return mediana

# FUNÇÃO LOCALIZAÇÃO DA MODA

def localiza_moda(valor: list, quantidade: int) -> str:

    """ Função para localizar a Moda em uma lista de dados. """

    lista_moda = [0]
    contador = 0
    contador_atual = 0
    validar_atual = 0

    for x in range(0, quantidade):
        validar = valor[x]

        if validar != validar_atual:

            if valor.count(validar) >= contador:
                contador = valor.count(validar)

                if contador > contador_atual and validar != lista_moda[0]:
                    lista_moda = []
                    lista_moda.append(validar)
                elif contador == contador_atual:
                    lista_moda.append(validar)
                validar_atual = validar
                contador_atual = contador

    return lista_moda