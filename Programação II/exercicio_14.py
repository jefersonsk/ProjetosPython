# Faça um algoritmo que receba o preço de custo de um produto, a quantidade em estoque e uma taxa de lucro em %. Informe qual será o lucro caso todo estoque seja vendido.

preco = float(input("Valor do Produto: R$ "))
quantidade = int(input("Quantidade em estoque: "))
taxa_lucro = float(input("Taxa de lucro (%): "))

total_venda = (preco * quantidade)
total_venda_lucro = ((total_venda * taxa_lucro) / 100) + total_venda

print(f"Total de vendas: R$ {total_venda_lucro:.2f}")