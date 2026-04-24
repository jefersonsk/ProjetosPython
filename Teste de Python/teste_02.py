# Sistema de Carrinho de Compras
# Objetivo: Somar o valor dos produtos e aplicar um cupom de desconto.

def adicionar_produto(nome, preco, quantidade, carrinho):

    novo_produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    # Adicionando o dicionário à lista do carrinho
    return carrinho.append(novo_produto)


def calcular_total(lista_produtos):
    total = 0
    for item in lista_produtos:
        # Somando o valor do item (preço * quantidade)
        total += item["preco"] * item["quantidade"]
    return total


def aplicar_desconto(valor_total, cupom):
    descontos = {"DESC10": 0.10, "DESC20": 0.20}

    try:
        valor_desconto = valor_total * descontos[cupom]
        novo_total = valor_total - valor_desconto
        return novo_total
    except KeyError:
        print("Aviso: Cupom não encontrado. O valor original será mantido.")
        return valor_total


carrinho = []

# Adicionando itens ao carrinho
adicionar_produto("Monitor", 800.00, 1, carrinho)
adicionar_produto("Mousepad", 50.00, 2, carrinho)

# Calculando e exibindo o total
total_compra = calcular_total(carrinho)
print(f"O total da compra é: R$ {total_compra}")

# Aplicando um cupom inexistente para testar o bloco try/except
total_com_desconto = aplicar_desconto(total_compra, "FALSO50")
print(f"Total a pagar: R$ {total_com_desconto}")
