# Faça um algoritmo que receba dois números e exiba o resultado da sua soma.

# map() aplica uma função especifica para cada item de uma lista, ou qualquer iterável, que retorno um resultado
# na linha abaixo cada valor digitado e transformado em float e atribuído a variável lista

lista = list(map(float, input("Digite 2 números: ").split(" ")))

print(f"Soma dos números: {sum(lista):.2f}")
