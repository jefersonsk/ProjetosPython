cobaias = {}

repeticoes = int(input())

for x in range(repeticoes):
    quantidade, tipo = input().upper().split(" ")
    if tipo not in cobaias:
        cobaias[tipo] = int(quantidade)
    else:
        soma = int(cobaias[tipo])
        soma = soma + int(quantidade)
        cobaias[tipo] = soma

total = cobaias['C'] + cobaias['R'] + cobaias["S"]
pct_coelhos = (cobaias['C'] * 100) / total
pct_sapos = (cobaias['S'] * 100) / total
pct_ratos = (cobaias['R'] * 100) / total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {cobaias['C']}")
print(f"Total de ratos: {cobaias['R']}")
print(f"Total de sapos: {cobaias['S']}")
print(f"Percentual de coelhos: {pct_coelhos:.2f} %")
print(f"Percentual de ratos: {pct_ratos:.2f} %")
print(f"Percentual de sapos: {pct_sapos:.2f} %")