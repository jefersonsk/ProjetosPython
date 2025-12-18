frase = input().strip()

frase = frase.replace(" ", "")
invertida = frase[::-1]

print(frase, invertida)

if frase == invertida:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")