renda_total = 0
renda_media = 0
pessoas = 0

with open('pessoas.csv', 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        nome = dados[0]
        renda = float(dados[6])
        renda_total = renda_total + renda
        pessoas += 1
        print(f"Processado: {nome} - R$ {renda:.2f}")

print("=" * 100)
print("Processamento finalizado...")
print(f"{pessoas} pessoas processadas.")
print(f"Renda média calculada: R$ {(renda_total/pessoas):.2f}")
    