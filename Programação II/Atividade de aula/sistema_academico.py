class Usuarios:
    def __init__(self, nome, senha, login):
        self.nome = nome
        self.senha = senha
        self.login = login

    def info(self):
        print(f"NOME: {self.nome}")
        print(f"LOGIN: {self.login}")
        print(f"SENHA: {self.senha}")

    def verifica_senha(self, login, senha):
        if login == self.login:
            if senha == self.senha:
                print("=== ACESSO PERMITIDO ===")
            else:
                print("=== SENHA INCORRETA ===")
        else:
            print("=== USUÁRIO NÃO ENCONTRADO ===")


class Alunos(Usuarios):
    def __init__(self, nome, senha, login, curso):
        super().__init__(nome, senha, login)
        self.curso = curso
        self.disciplinas = []

    def solicita_matricula(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.adicionar_aluno(self)

    def info(self):
        print("-----> INFORMAÇÕES ALUNO")
        super().info()
        print(f"CURSO: {self.curso}")
        print("-----> DISCIPLINA MATRICULADA")
        for disciplina in self.disciplinas:
            print(f"DISCIPLINA: {disciplina.nome}")
        print()


class Professores(Usuarios):
    def __init__(self, nome, senha, login, area):
        super().__init__(nome, senha, login)
        self.area = area
        self.disciplinas = []

    def aloca_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.adicionar_professor(self)

    def info(self):
        print("-----> INFORMAÇÕES DO PROFESSOR")
        super().info()
        print(f"ÁREA: {self.area}")
        print("-----> DISCIPLINAS MINISTRADAS")
        for disciplinas in self.disciplinas:
            print(f"DISCIPLINA: {disciplinas.nome}")
        print()


class Disciplinas:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None
        self.alunos_matriculados = []

    def adicionar_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)

    def adicionar_professor(self, professor):
        self.professor = professor

    def info(self):
        print("-----> DADOS DA AULA")
        print(f"DISCIPLINA: {self.nome}")
        print(f"PROFESSOR: {self.professor.nome}")
        for aluno in self.alunos_matriculados:
            print(f"ALUNOS: {aluno.nome}")
        print()


if __name__ == "__main__":
    aluno_01 = Alunos("Jeferson", "1234", "jefo", "ADS")
    aluno_02 = Alunos("Pipe", "4321", "pixurico", "Fundamental")
    aluno_03 = Alunos("Tuti", "games", "tutinho", "Fundamental")
    professor_01 = Professores("Edna", "2330", "edn@", "Alfabetização")
    professor_02 = Professores("Ricardo", 8877, "Rick", "Programação")

    disciplina_01 = Disciplinas("Prog II")
    disciplina_02 = Disciplinas("Turma 11")
    disciplina_03 = Disciplinas("Turma 12")

    professor_01.aloca_disciplina(disciplina_02)
    professor_01.aloca_disciplina(disciplina_03)
    professor_02.aloca_disciplina(disciplina_01)

    aluno_01.solicita_matricula(disciplina_01)
    aluno_02.solicita_matricula(disciplina_02)
    aluno_03.solicita_matricula(disciplina_02)

    aluno_01.info()
    professor_01.info()

    disciplina_01.info()
    disciplina_02.info()

    print("VERIFICAÇÃO DE SENHA")
    print("=" * 30)
    print(f"NOME ALUNO: {aluno_01.nome}")
    aluno_01.verifica_senha("jefo", "1234")
    print(f"NOME PROFESSOR: {professor_01.nome}")
    professor_01.verifica_senha("edn@", "2370")
