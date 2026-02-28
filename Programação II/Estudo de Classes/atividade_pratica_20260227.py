class Empresa:
    def __init__(self, nome, cnpj, endereco, servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico

class Remedio:
    def __init__(self, nome, tarja, valor, laboratorio, estoque):
        self.nome = nome
        self.tarja = tarja
        self.valor = valor
        self.laboratorio = laboratorio
        self.estoque = estoque

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, salario, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

class Livro:
    def __init__(self, titulo, isbn, valor, autor, editora, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.estoque = estoque

if __name__ == "__main__":
    dado_empresa_01 = Empresa(nome="Terra", cnpj="988376654", endereco="Rua Treze, 12", servico="Portal de Notícias")
    dado_empresa_02 = Empresa(nome="Blockbuster", cnpj="99887766", endereco="Rua AAAA, 76", servico="Locadora")
    dado_empresa_03 = Empresa(nome="Blizzard", cnpj="98236423864", endereco="Av. Limeira, 11", servico="Jogos")

    dado_remedio_01 = Remedio(nome="Rivaroxabana", tarja="Vermelha", valor=34, laboratorio="EMS", estoque=3)
    dado_remedio_02 = Remedio(nome="Dorflex", tarja="Verde", valor=25.9, laboratorio="Ginger", estoque=10)
    dado_remedio_03 = Remedio(nome="ASS",tarja="Amarela", valor=5.90, laboratorio="Génerico", estoque=50)

    dado_funcionario_01 = Funcionario(nome="Jeferson", sobrenome="Silveira", cpf="8966355636", salario=3000, cargo="Analista")
    dado_funcionario_02 = Funcionario(nome="Edna", sobrenome="Silva", cpf="98793874982", salario=6000, cargo="Professora")
    dado_funcionario_03 = Funcionario(nome="Jorge", sobrenome="Kendzierski", cpf="83483837948", salario=3300, cargo="Aposentado")

    dado_livro_01 = Livro(titulo="Rambo", isbn=980234283, valor=59.90, autor="John C.", editora="Pipoca e Nanquim", estoque=0)
    dado_livro_02 = Livro(titulo="Senhor dos Anéis", isbn=98239834, valor=110.90, autor="Tolkien", editora="Futuro", estoque=20)
    dado_livro_03 = Livro(titulo="Xmen", isbn=8034032974, valor=129.90, autor="Stan Lee", editora="Panini", estoque=15)

    print("EMPRESAS")
    print("--------------")
    print(dado_empresa_01.nome)
    print(dado_empresa_01.cnpj)
    print(dado_empresa_01.endereco)
    print(dado_empresa_01.servico)
    print(dado_empresa_02.nome)
    print(dado_empresa_02.cnpj)
    print(dado_empresa_02.endereco)
    print(dado_empresa_02.servico)
    print(dado_empresa_03.nome)
    print(dado_empresa_03.cnpj)
    print(dado_empresa_03.endereco)
    print(dado_empresa_03.servico)

    print("--------------")
    print("REMÉDIOS")
    print("--------------")
    print(dado_remedio_01.nome)
    print(dado_remedio_01.tarja)
    print(dado_remedio_01.valor)
    print(dado_remedio_01.laboratorio)
    print(dado_remedio_01.estoque)
    print(dado_remedio_02.nome)
    print(dado_remedio_02.tarja)
    print(dado_remedio_02.valor)
    print(dado_remedio_02.laboratorio)
    print(dado_remedio_02.estoque)
    print(dado_remedio_03.nome)
    print(dado_remedio_03.tarja)
    print(dado_remedio_03.valor)
    print(dado_remedio_03.laboratorio)
    print(dado_remedio_03.estoque)

    print("--------------")
    print("FUNCIONÁRIOS")
    print("--------------")
    print(dado_funcionario_01.nome)
    print(dado_funcionario_01.sobrenome)
    print(dado_funcionario_01.cpf)
    print(dado_funcionario_01.salario)
    print(dado_funcionario_01.cargo)
    print(dado_funcionario_02.nome)
    print(dado_funcionario_02.sobrenome)
    print(dado_funcionario_02.cpf)
    print(dado_funcionario_02.salario)
    print(dado_funcionario_02.cargo)
    print(dado_funcionario_03.nome)
    print(dado_funcionario_03.sobrenome)
    print(dado_funcionario_03.cpf)
    print(dado_funcionario_03.salario)
    print(dado_funcionario_03.cargo)

    print("--------------")
    print("LIVROS")
    print("--------------")
    print(dado_livro_01.titulo)
    print(dado_livro_01.isbn)
    print(dado_livro_01.valor)
    print(dado_livro_01.autor)
    print(dado_livro_01.editora)
    print(dado_livro_01.estoque)
    print(dado_livro_02.titulo)
    print(dado_livro_02.isbn)
    print(dado_livro_02.valor)
    print(dado_livro_02.autor)
    print(dado_livro_02.editora)
    print(dado_livro_02.estoque)
    print(dado_livro_03.titulo)
    print(dado_livro_03.isbn)
    print(dado_livro_03.valor)
    print(dado_livro_03.autor)
    print(dado_livro_03.editora)
    print(dado_livro_03.estoque)