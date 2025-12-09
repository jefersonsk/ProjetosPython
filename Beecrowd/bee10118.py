valor = int(input())

print(valor)
auxiliar = valor // 100
print(f"{auxiliar} nota(s) de R$ 100,00")
valor = valor - (auxiliar * 100)
auxiliar = valor // 50
print(f"{auxiliar} nota(s) de R$ 50,00")
valor = valor - (auxiliar * 50)
auxiliar = valor // 20
print(f"{auxiliar} nota(s) de R$ 20,00")
valor = valor - (auxiliar * 20)
auxiliar = valor // 10
print(f"{auxiliar} nota(s) de R$ 10,00")
valor = valor - (auxiliar * 10)
auxiliar = valor // 5
print(f"{auxiliar} nota(s) de R$ 5,00")
valor = valor - (auxiliar * 5)
auxiliar = valor // 2
print(f"{auxiliar} nota(s) de R$ 2,00")
valor = valor - (auxiliar * 2)
print(f"{valor} nota(s) de R$ 1,00")