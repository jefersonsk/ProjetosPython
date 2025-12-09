soma_pares = 0
produto_impares = 1

numero_final = int(input())

for x in range(1, numero_final +1):
    if x % 2 == 0:
        soma_pares = soma_pares + x
    else:
        produto_impares = produto_impares * x

print(soma_pares)
print(produto_impares)