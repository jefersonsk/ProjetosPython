
DESCONTO_PADRAO = 0.10

produto = input("Produto: ")
preco = float(input("Preço (em R$): "))
quantidade = int(input("Quantidade: "))

total_bruto = preco * quantidade
total_liquido = total_bruto * (1 - DESCONTO_PADRAO)

print("\n--- RECIBO ---")
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total Bruto: {total_bruto:.2f}")
print(f"Desconto: ({DESCONTO_PADRAO * 100:.0f}%): R$ {total_bruto - total_liquido:.2f}")
print(f"Total a pagar: R$ {total_liquido:.2f}")
