salario = float(input())

if salario <= 400:
    reajuste = salario * 0.15
    faixa = 15
elif salario <= 800:
    reajuste = salario * 0.12
    faixa = 12
elif salario <= 1200:
    reajuste = salario * 0.1
    faixa = 10
elif salario <= 2000:
    reajuste = salario * 0.07
    faixa = 7
else:
    reajuste = salario * 0.04
    faixa = 4

print(f"Novo salario: {(salario + reajuste):.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {faixa} %")