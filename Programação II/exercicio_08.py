# Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.

# Na linha abaixo o map() transforma cada dado digitado em float para ser armazendo na variável lista.

lista = list(map(float, input("Digite 2 números: ").split(" ")))

print(f"Soma: {sum(lista)}")
print(f"Subtração: {lista[0] - lista[1]}")
print(f"Multiplicação: {lista[0] * lista[1]}")
print(f"Divisão: {lista[0] / lista[1]}")
