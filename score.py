dados_jogador = input()
nome, posicao, min_jogados, dist_km, sprints, vel_max_kmh, gols, assist, passes_certos, passes_totais, chutes_no_alvo, duelos_ganhos, duelos_totais, interceptacoes, desarmes, erros_decisivos = dados_jogador.split(";")

gols_norm = int(gols) * 2
assistencias = int(assist) * 1.2
precisao_de_passes = (int(passes_certos) / int(passes_totais)) * 3
duelos_vencidos = (int(duelos_ganhos) / int(duelos_totais)) * 1
sprints_norm = (int(sprints) / 30) * 1
distancia_percorrida = (float(dist_km) / 12) * 1
finalizacoes = (int(chutes_no_alvo) / 5) * 0.8
acoes_defensivas = ((int(interceptacoes) + int(desarmes)) / 10) * 1
# velocidade_maxima = (float(vel_max_kmh) - 28)/10 + (float(vel_max_kmh) > 28 * 0.5)
velocidade_maxima = float(vel_max_kmh - 28) / 10
velocidade_maxima_bonus = velocidade_maxima > 0 * 0.5
erros_decisivos_norm = int(erros_decisivos) + (int(erros_decisivos) <= 3) * - 1.5
passes_pct = (int(passes_certos) * 100) / int(passes_totais)
duelos_pct = (int(duelos_ganhos) * 100) / int(duelos_totais)
nota_bruta = (3.0 + gols_norm + assistencias + precisao_de_passes + duelos_vencidos + sprints_norm + distancia_percorrida + finalizacoes + acoes_defensivas + velocidade_maxima_bonus - erros_decisivos_norm) / 16

print(f'RESUMO: {nome.title()} — POS: {posicao.upper()}')
print(f'MINUTOS: {min_jogados}')
print(f'DIST_KM: {float(dist_km):.3f} — SPRINTS: {sprints} — VEL_MAX_KMH: {float(vel_max_kmh):.1f}')
print(f'PASSES: {passes_certos}/{passes_totais} ({passes_pct:.1f}%)')
print(f'DUELOS: {duelos_ganhos}/{duelos_totais} ({duelos_pct:.1f}%)')
print(f'OFENSIVO: GOLS={gols} ASSIST={assist} CHUTES_NO_ALVO={chutes_no_alvo}')
print(f'DEFENSIVO: INTERCEPTACOES={interceptacoes} DESARMES={desarmes}')
print(f'ERROS_DECISIVOS: {int(erros_decisivos)}')
print(f'NOTA: {10 - nota_bruta:.2f}/10')


vel_max_kmh = 29
vel_max_norm = (vel_max_kmh - 28) / 10

validar_velocidade = int(vel_max_kmh > 28) * vel_max_kmh