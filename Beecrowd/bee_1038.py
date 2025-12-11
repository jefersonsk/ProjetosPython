lanches = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

escolha, quantidade = map(int, input().split(" "))

valor = lanches[escolha]

total = valor * quantidade

print(f"Total: R$ {total:.2f}")