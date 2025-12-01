print('Times do Campeonato Brasileiro\n')

nome_time = input('Digite o nome do time: ')

# colocar todos os caracteres em minúsculo com lower()
nome_time = nome_time.lower()

# colocar a primeira letra de cada palavra em maiúscula e o restante em minúsculo com title()
nome_normalizado = nome_time.title()

# valida com find() se exite o 'fc' na string 
tem_fc = nome_time.find("fc") >= 0

# verifica com [0] se a string começa com 's'
comeca_s = nome_time[0] == "s"

# verifica se o nome termina com 'ense' utilizando []
termina_ense = nome_time[-4:] == "ense"

# verifica com find() se tem a palavra 'clube' na string
tem_clube = nome_time.find("clube") >= 0

# verifica com find() se tem a palavra 'atletico' ou 'atlético' na string
tem_atletico = nome_time.find("atletico") >= 0 or nome_time.find("atlético") >= 0

# verifica se a string tem menos de 10 caracteres, utilizando len() para retornar o tamanho total e count() para diminiur do cálculo os espaços
nome_curto = (len(nome_time) - nome_time.count(" ")) < 10

# retira os espaços da string com replace()
nome_valido = nome_time.replace(" ", "")

# valida se a string tem somente letras com isalpha()
nome_valido = nome_valido.isalpha()

# verifica se tem 'gremio' ou 'grêmio' na string com find()
tem_gremio = nome_time.find("gremio") >= 0 or nome_time.find("grêmio") >= 0

# valida tem tem 'fc', 'clube', 'gremio' ou é > 10
destaque = (tem_fc == True or tem_clube == True or tem_gremio == True) and nome_curto == False

print('\n')
print(f'NOME_NORMALIZADO: {nome_normalizado}')
print(f'TEM_FC: {tem_fc}')
print(f'COMECA_COM_S: {comeca_s}')
print(f'TERMINA_COM_ENSE: {termina_ense}')
print(f'TEM_CLUBE: {tem_clube}')
print(f'TEM_ATLETICO: {tem_atletico}')
print(f'NOME_CURTO: {nome_curto}')
print(f'NOME_VALIDO: {nome_valido}')
print(f'DESTAQUE: {destaque}')