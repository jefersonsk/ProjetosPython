x = int(input())

if 0 < x < 1000000:
    notas_100 = x // 100
    x = x % 100
    print(x)
    notas_50 = x // 50
    x = x % 50
    notas_20 = x // 20
    x = x % 20
    notas_10 = x // 10
    x = x % 10
    notas_5 = x // 5
    x = x % 5
    notas_2 = x // 2
    x = x % 2
    notas_1 = x // 1
    x = x % 1
    print(f"{notas_100} nota(s) de R$ 100,00")
    print(f"{notas_50} nota(s) de R$ 50,00")
    print(f"{notas_20} nota(s) de R$ 20,00")
    print(f"{notas_10} nota(s) de R$ 10,00")
    print(f"{notas_5} nota(s) de R$ 5,00")
    print(f"{notas_2} nota(s) de R$ 2,00")
    print(f"{notas_1} nota(s) de R$ 1,00")
else:
    print("Valor inválido! Deve ser entre 0 e 1.000.000") 
