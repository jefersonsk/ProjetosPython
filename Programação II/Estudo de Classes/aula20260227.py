class Aluno:
    def __init__(self, nome, curso, matricula): # Método construtor
        self.nome = nome # isso é um atributo
        self.curso = curso
        self.matricula = matricula

if __name__ == "__main__": # Se não for o programa principal, essa parte não é executada
    a1 = Aluno("jeferson", "ADS", "1234")
    print(a1.nome)
    print(a1.curso)
    print(a1.matricula)

    a2 = Aluno(matricula="2345", nome="Edna", curso="ADS") # forma explícita de se utilizar
    print(a2.nome)
    print(a2.curso)
    print(a2.matricula)