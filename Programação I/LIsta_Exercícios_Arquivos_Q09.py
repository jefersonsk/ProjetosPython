def imprime_texto(nome: str, idade: int, profissao: str) -> str:
    return print(f"{nome}, {idade} anos, profissão: {profissao}")

with open("consultas.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        aux_nome = dados[0]
        aux_idade = dados[1]
        aux_profissao = dados[2]
        imprime_texto(aux_nome, aux_idade, aux_profissao)

arquivo.close()