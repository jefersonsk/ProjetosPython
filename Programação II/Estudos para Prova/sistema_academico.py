class Usuario:
    def __init__(self, nome, senha, login):
        self.nome = nome
        self.senha = senha
        self.login = login

    def __str__(self):
        return (
            f"NOME: {self.nome}\n"
            f"SENHA: {self.senha}\n"
            f"LOGIN: {self.login}\n"
        )

    def verifica_senha(self):
        pass


class Aluno(Usuario):
    def __init__(self, nome, senha, login, curso):
        super().__init__(nome, senha, login)
        self.curso = curso
        self.disciplinas = []

    def __str__(self):
        lista_disciplinas = "\nDisciplinas: "

        for disciplina in self.disciplinas:
            lista_disciplinas += f"\n - {disciplina.nome}"

        return (
            super().__str__() +
            f"{self.curso}" +
            lista_disciplinas
        )

    def solicita_matricula(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.alunos.append(self)


class Professor(Usuario):
    def __init__(self, nome, senha, login, area):
        super().__init__(nome, senha, login)
        self.area = area
        self.disciplinas = []

    def __str__(self):
        return (
            ">>> Professor(a) <<<\n" +
            super().__str__() +
            f"ÁREA: {self.area}\n" +
            50 * "-"
        )

    def aloca_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.professor = self


class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def info_disciplina(self):
        lista_alunos = "\nAlunos Matriculados:"
        print(f">>> Disciplina {self.nome}")
        print(f"Professor: {self.professor.nome}")

        for aluno in self.alunos:
            lista_alunos += f"\n - {aluno.nome}"

        print(lista_alunos)


if __name__ == "__main__":
    # Criando Alunos
    aluno_01 = Aluno("Jeferson", 1234, "jefosk", "Pedagogia")
    aluno_02 = Aluno("Pipe", 324, "pipegamer", "Pedagogia")
    aluno_03 = Aluno("Tuti", 1234, "tutinho", "Pedagogia")
    aluno_04 = Aluno("Serginho", 334445, "miguelzinho", "Pedagogia")

    # Criando Professores
    professor_01 = Professor("Edna", 2330, "didi", "Pedagoga")

    # Criando Disciplinas
    disciplina_01 = Disciplina("Alfabetização", professor_01)
    disciplina_02 = Disciplina("Leitura", professor_01)

    # Matriculando Alunos
    aluno_01.solicita_matricula(disciplina_01)
    aluno_02.solicita_matricula(disciplina_01)
    aluno_03.solicita_matricula(disciplina_01)
    aluno_04.solicita_matricula(disciplina_01)
    aluno_01.solicita_matricula(disciplina_02)

    # Alocando Professores
    professor_01.aloca_disciplina(disciplina_01)
    professor_01.aloca_disciplina(disciplina_02)

    print(aluno_01)
    print(professor_01)

    disciplina_01.info_disciplina()
