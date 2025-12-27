quantidade = int(input())

for x in range(quantidade):
    anos = 0
    cidade_a, cidade_b, crescimento_a, crescimento_b = map(float, input().split(" "))

    while cidade_a <= cidade_b:
        total_a = (crescimento_a * cidade_a) / 100
        total_a = total_a - (total_a % 1)
        cidade_a += total_a
        total_b = (crescimento_b * cidade_b) / 100
        total_b = total_b - (total_b % 1)
        cidade_b += total_b
        anos += 1

    if anos <= 100:
        print(f"{anos} anos.")
    if anos > 100:
        print("Mais de 1 seculo.") 
