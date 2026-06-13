import mysql.connector
from mysql.connector import Error
from utilidades import (
    imprimir_cabecalho,
    criar_menu,
    verificar_numero,
    verificar_vazio,
    enter_para_sair,
    pausar,
    continuar,
    imprimir_linha,
    mostrar_erro,
    validar_cpf,
    Cor
)


class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota Inválida")


aluno01 = Avaliacao("Jeferson", "Matemática")
aluno01.nota = 50

print(f"🏦 O aluno {aluno01.nome} esta com a nota {aluno01.nota}"
      f" na disciplina {aluno01.disciplina}")


class BancoDeDados:
    def __init__(self, host, user, password, nome_banco):
        self.host = host
        self.user = user
        self.password = password
        self.nome_banco = nome_banco

        def iniciar_banco(self):
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.nome_banco
            )

    def consultar_banco_sql(dados: str | int, tipo: str) -> tuple | None:
        lista_de_permissao = ("id", "cpf")
        meu_banco = None
        mycursor = None

        if tipo not in lista_de_permissao:
            mostrar_erro("E02", Cor.VERMELHO)
            return
        try:
            meu_banco = iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_consulta = f"SELECT * FROM funcionarios WHERE {tipo} = %s"
            mycursor.execute(comando_sql_consulta, [dados])
            resultado_cosulta = mycursor.fetchone()

            return resultado_cosulta

        except Error as erro:
            print(f"\n❌ Erro crítico ao acessar o banco de dados:")
            print(f"{Cor.AMARELO}{erro}{Cor.RESET}")
            return

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()
