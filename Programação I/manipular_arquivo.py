arquivo = open('novo_arquivo.txt', 'r')

contador = 0
acumulador = 0

# local = int(input("Qual linha quer retornar na tela: "))
# print("=" * 100)

for linha in arquivo:
    x = linha.count(" ")
    contador += 1
    print(f"{contador}: {linha}", end="")
    acumulador = acumulador + x

arquivo.close()

print()

print("=" * 100)
print(f"O arquivo possui {contador} linhas.")
print(acumulador + 1)