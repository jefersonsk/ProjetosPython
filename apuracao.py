dados_eleicao = input()
zona, secao, eleitores, c1_nome, c1_votos, c2_nome, c2_votos, c3_nome, c3_votos, brancos, nulos = dados_eleicao.split(";")

total_votos = int(c1_votos) + int(c2_votos) + int(c3_votos) + int(brancos) + int(nulos)
participacao = (total_votos * 100) / int(eleitores)
votos_validos = total_votos - int(brancos) - int(nulos)
c1_votos_pct = (int(c1_votos) * 100) / votos_validos
c2_votos_pct = (int(c2_votos) * 100) / votos_validos
c3_votos_pct = (int(c3_votos) * 100) / votos_validos
brancos_pct = (int(brancos) * 100) / total_votos
nulos_pct = (int(nulos) * 100) / total_votos
maioria_absoluta = (c1_votos_pct > 50) or (c2_votos_pct > 50) or (c3_votos_pct > 50)
consistente = eleitores > total_votos

print(total_votos)
print(participacao)
print(votos_validos)
print(c1_votos_pct)
print(c2_votos_pct)
print(c3_votos_pct)
print(brancos_pct)
print(nulos_pct)
print(maioria_absoluta)
print(consistente)
