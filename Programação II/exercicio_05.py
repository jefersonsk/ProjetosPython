# Declare cinco variáveis do tipo inteiro, realize a soma e exiba na tela.

# map(função, iterável) aplica uma função específica para cada item de uma lista, ou qualquer outro iterável e devolve o resultado.
# No comando abaixo esta transformando os dados digitados em inteiro, que estão sendo adicionados na variável lista.

lista = list(map(int, input("Digite 5 numeros: ").split(" ")))

print(f"Soma dos números digitados: {sum(lista)}")