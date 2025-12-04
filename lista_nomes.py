nomes = []
lista_tamanho = {}

numero = int(input())

for x in range(0, numero):
    nome = input()
    lista_tamanho[nome] = len(nome)

print(lista_tamanho)