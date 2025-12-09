from datetime import datetime

usuario = ""
agora = ""
registro = [usuario, agora]

with open("logs.txt", "a") as arquivo:
    usuario = input("Digite seu usuário: ").lower()
    agora = datetime.now()
    registro = [usuario, agora.strftime("%d/%m/%Y às %H:%M")]
    linha = ' - '.join(registro)
    arquivo.write(linha + '\n')

arquivo.close()