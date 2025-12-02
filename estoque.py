produto = "Produto"
preco = "Preço"
quantidade = "Quantidade"
registro = [produto, preco, quantidade]
repetir = "S"
valor_total = 0

with open('produtos.csv', 'w') as arquivo:
    linha = ','.join(registro)
    arquivo.write(linha + "\n")
    while repetir != "N":
        produto = input("Produto: ")
        preco = input("Preço: ")
        quantidade = input("Quantidade: ")
        registro = [produto, preco, quantidade]
        valor_total = valor_total + (float(preco) * int(quantidade))
        linha = ','.join(registro)
        arquivo.write(linha + "\n")
        repetir = input("Repetir S/N?\n").upper()

print("Processamento concluído!")
print(f"Valor total do estoque: R$ {valor_total:.2f}")