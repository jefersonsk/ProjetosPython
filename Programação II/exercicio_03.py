# Receba o nome, sobrenome, sexo, RG e idade e posteriormente exiba as informações na tela. Nome e sobrenome devem ser informados na mesma linha.

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
sexo = input("Digite o sexo: ")
rg = int(input("Digite o RG: "))
idade = int(input("Digite a idade: "))

print(f"Nome completo: {nome} {sobrenome}")
print(f"Sexo: {sexo}")
print(f"RG: {rg}")
print(f"Idade: {idade}")