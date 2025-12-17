quantidade = int(input())

for x in range(quantidade):
    nota_01, nota_02, nota_03 = map(float, input().split(" "))
    media = (nota_01 * 2 + nota_02 * 3 + nota_03 * 5) / 10
    print(f"{media:.1f}")