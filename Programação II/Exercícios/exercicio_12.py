# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, 
# meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

lista_idade = list(map(int, input("Digite sua idade em anos, meses e dias: ").split(" ")))

total_dias = (lista_idade[0] * 365) + (lista_idade[1] * 30) + lista_idade[2]

print(f"Idade em dias: {total_dias}")