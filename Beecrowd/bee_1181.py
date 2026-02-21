soma = 0
media = 0

linha = int(input())
operacao = input()

for x in linha:
    soma += x

if operacao.upper() == 'S':
    print(f"{soma:.1f}")
else:
    media = soma / 12
    print(f"{media:.1f}")