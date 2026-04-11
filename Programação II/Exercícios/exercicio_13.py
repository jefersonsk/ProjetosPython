# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salario = float(input("Digite o salário: R$ "))
reajuste = float(input("Digite o percentual de reajuste (%): "))

salario_reajustado = ((reajuste * salario) / 100) + salario

print(f"Salário reajustado: R$ {salario_reajustado:.2f}")