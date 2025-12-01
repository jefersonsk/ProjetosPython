valor_reais = float(input('Digite o valor em reais: R$ '))
cotacao_dolar = float(input('Digite a cotação Dólar(USD) em reais: R$ '))
cotacao_euro = float(input('Digite cotação Euro(EUR) em reais: R$ '))
meta_dolar = float(input('Digite meta Dólar: USD '))
meta_euro = float(input('Digite meta Euro: EUR '))

total_dolar = valor_reais / cotacao_dolar
total_euro = valor_reais / cotacao_euro

usd_maior_que_eur = total_dolar > total_euro
atinge_meta_usd = total_dolar > meta_dolar
atinge_meta_eur = total_euro > meta_euro
ambas_metas = atinge_meta_usd == True and atinge_meta_eur == True

print('\n')
print(f'USD {total_dolar:.2f}')
print(f'EUR {total_euro:.2f}')
print(f'usd_maior_que_eur: {usd_maior_que_eur}')
print(f'atinge_meta_usd: {atinge_meta_usd}')
print(f'atinge_meta_eur: {atinge_meta_eur}')
print(f'atinge_ambas_as_metas: {ambas_metas}')