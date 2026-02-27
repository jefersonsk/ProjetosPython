# Receba três nomes e exiba os mesmos separando os por virgulas.

lista = list(input("Digite 3 nomes separados por espaço: ").split(" "))
print(*lista, sep=", ") #* na frente a lista tira os colchetes e sep define o separador entre os dados printados