numeros = sorted(list(map(int, input().split(" "))), reverse=True)

print("Sao Multiplos" if numeros[0] % numeros[1] == 0 else "Nao sao Multiplos")