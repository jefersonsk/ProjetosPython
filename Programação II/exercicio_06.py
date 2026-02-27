# Declare cinco variáveis do tipo float, realize a soma e exiba na tela.

lista = []

for x in range(5):
    lista.append(float(input(f"Digite o {x + 1}º númnero: ")))

print(f"Soma dos número: {sum(lista):.2f}")