fibonacci = [0, 1]

quantidade = int(input())

lista = [int(input()) for x in range(quantidade)]

for x in lista:

    for y in range(len(fibonacci), x + 1):
        numero_fibonacci = fibonacci[y - 1] + fibonacci[y - 2]
        fibonacci.append(numero_fibonacci)

    print(f"Fib({x}) = {fibonacci[x]}")