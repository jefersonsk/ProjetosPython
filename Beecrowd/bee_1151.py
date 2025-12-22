fibonacci = [0, 1]

numero = int(input())

for x in range(2, numero):
    proximo = fibonacci[x - 1] + fibonacci[x -2]
    fibonacci.append(proximo)

print(*fibonacci[:numero])