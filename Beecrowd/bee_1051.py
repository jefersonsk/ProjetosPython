imposto = 0

salario = float(input())

if salario > 4500:
    imposto += 1500 * 0.18
    base_28_pct = salario - 4500
    imposto += base_28_pct * 0.28
elif salario > 3000:
    imposto += 1000 * 0.08
    base_18_pct = salario - 3000
    imposto += base_18_pct * 0.18
elif salario > 2000:
    base_08_pct = salario - 2000
    imposto += base_08_pct * 0.08

print(imposto)