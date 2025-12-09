dados_usuario = input()

usuario, senha = dados_usuario.split(";")
comprimento = len(senha) < 64 and len(senha) > 12
tem_maiuscula = "1357".find(senha)



print(tem_maiuscula)