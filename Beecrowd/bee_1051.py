def calcular_imposto(salario: float) -> float:
    imposto = 0

    if salario > 4500:
        imposto += 1000 * 0.08
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

    return imposto

def verifica_positivo() -> float:
    while True:

        try:
            valor = float(input())

            if valor < 0:
                raise ValueError("Valor precisa ser um número positivo")
            else:
                return valor
            
        except (ValueError, TypeError):
            print("ERRO: Valor inválido!")            

salario = verifica_positivo()

imposto = calcular_imposto(salario)

print(f"R$ {imposto:.2f}" if imposto > 0 else "Isento")