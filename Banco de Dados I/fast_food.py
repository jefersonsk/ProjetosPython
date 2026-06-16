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
    imprimir_dados_na_tela,
    escolher_categoria,
    escolher_orgao_emissor,
    Cor
)
from mysql.connector import Error
import mysql.connector
import os

# Para chamar as variáveis de ambiente precisa fazer esssa instalção
# pip install python-dotenv
from pathlib import Path
from dotenv import load_dotenv

# 1. Pega a pasta exata onde este script (main) está salvo
pasta_do_script = Path(__file__).parent

# 2. Junta essa pasta com o nome do arquivo secreto
caminho_env = pasta_do_script / ".env"

# 3. Força o carregamento a partir desse caminho exato
load_dotenv(caminho_env)


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

    def inserir_orgao_sql(self, novo_orgao):
        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            dados = (
                novo_orgao.nome_orgao
            )
            comando_sql_insercao = """
                INSERT INTO orgaos_emissores
                    (
                        orgao_emissor    
                    )
                VALUES
                    (%s)
            """

            mycursor.execute(comando_sql_insercao, [dados])
            meu_banco.commit()

        except Error as erro:
            print(f"\n❌ Erro crítico ao salvar no banco de dados: {erro}")

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()

    def inserir_funcionario_sql(self, novo_funcionario):

        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            dados = (novo_funcionario.nome,
                     novo_funcionario.cpf,
                     novo_funcionario.rg,
                     novo_funcionario.orgaos_emissores_id,
                     novo_funcionario.categoria_funcional,
                     novo_funcionario.salario
                     )
            comando_sql_insercao = """
                INSERT INTO funcionarios
                    (
                        nome,
                        cpf,
                        rg,
                        orgaos_emissores_id,
                        categoria_funcional,
                        salario
                    )
                VALUES
                    (%s, %s, %s, %s, %s, %s)
            """
            mycursor.execute(comando_sql_insercao, dados)
            meu_banco.commit()

        except Error as erro:
            print(f"\n❌ Erro crítico ao salvar no banco de dados: {erro}")

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()

    def consultar_funcionario_sql(
        self, dados: str | int, tipo: str
    ) -> tuple | None:

        lista_de_permissao = ("id", "cpf")
        meu_banco = None
        mycursor = None

        if tipo not in lista_de_permissao:
            mostrar_erro("E02", Cor.VERMELHO)
            return
        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_consulta = (
                f"SELECT * FROM funcionarios WHERE {tipo} = %s"
            )
            mycursor.execute(comando_sql_consulta, [dados])
            resultado_consulta = mycursor.fetchone()

            return resultado_consulta

        except Error as erro:
            print(f"\n❌ Erro crítico ao acessar o banco de dados:")
            print(f"{Cor.AMARELO}{erro}{Cor.RESET}")
            return

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()

    def excluir_funcionario_sql(self, dados: str):

        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_exclusao = "DELETE FROM funcionarios WHERE id = %s"
            mycursor.execute(comando_sql_exclusao, [dados])
            meu_banco.commit()

        except Error as erro:
            print(f"\n❌ Erro crítico ao excluir no banco de dados: {erro}")
            return

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()

    def alterar_funcionario_sql(
        self, id: str | int, coluna: str, novo_valor: str
    ):

        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_consulta = (
                f"UPDATE funcionarios SET {coluna} = %s WHERE id = %s"
            )
            mycursor.execute(comando_sql_consulta, [novo_valor, id])
            meu_banco.commit()

        except Error as erro:
            print(f"\n❌ Erro crítico ao acessar o banco de dados:")
            print(f"{Cor.AMARELO}{erro}{Cor.RESET}")
            return

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()

    def listar_orgaos_sql(self) -> list | None:

        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_consulta = (
                "SELECT * FROM orgaos_emissores"
            )
            mycursor.execute(comando_sql_consulta)
            resultado_cosulta = mycursor.fetchall()

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

    def consultar_orgao_sql(self, dados: str):

        meu_banco = None
        mycursor = None

        try:
            meu_banco = self.iniciar_banco()
            mycursor = meu_banco.cursor()
            comando_sql_consulta = (
                f"SELECT * FROM orgaos_emissores WHERE id = %s"
            )
            mycursor.execute(comando_sql_consulta, [dados])
            resultado_consulta = mycursor.fetchone()

            return resultado_consulta[1]

        except Error as erro:
            print(f"\n❌ Erro crítico ao excluir no banco de dados: {erro}")
            return

        finally:
            if mycursor is not None:
                mycursor.close()

            if meu_banco is not None:
                meu_banco.close()


class Funcionarios:
    def __init__(
        self, nome, cpf, rg, orgaos_emissores_id, categoria_funcional, salario
    ):

        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.orgaos_emissores_id = orgaos_emissores_id
        self.categoria_funcional = categoria_funcional
        self.salario = salario


class Sistema:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def cadastrar_orgao(self):

        while True:
            flag = False
            imprimir_cabecalho("CADASTRO DE ÓRGÃO EMISSOR", cor=Cor.LARANJA)

            nome_orgao_digitado = enter_para_sair("NOME ÓRGÃO: ", cor=Cor.AZUL)

            if not nome_orgao_digitado:
                return

            lista_orgaos = self.nome_banco.listar_orgaos_sql()

            for orgao in lista_orgaos:
                if nome_orgao_digitado == orgao[1]:
                    flag = True

            if flag:
                mostrar_erro("E07", cor=Cor.AMARELO)
                continue

            novo_orgao = OrgaoEmissor(nome_orgao_digitado)
            self.nome_banco.inserir_orgao_sql(novo_orgao)

            imprimir_cabecalho("ORGÃO EMISSOR SALVO COM SUCESSO.")

            pausar()

            if continuar():
                continue
            else:
                return

    def cadastrar_funcionario(self):
        while True:
            imprimir_cabecalho("CADASTRO DE FUNCIONÁRIOS", cor=Cor.LARANJA)

            cpf = validar_cpf("CPF", Cor.CIANO)

            if not cpf:
                return

            lista_de_orgaos = self.nome_banco.listar_orgaos_sql()

            if not lista_de_orgaos:
                mostrar_erro("E08", cor=Cor.AMARELO)
                break

            resultado_busca = self.nome_banco.consultar_funcionario_sql(
                cpf, "cpf")

            if resultado_busca:
                mostrar_erro("E01", Cor.AMARELO)
                continue

            nome = verificar_vazio("NOME: ", Cor.CIANO)
            rg = verificar_vazio("RG: ", Cor.CIANO)
            nome_orgao = escolher_orgao_emissor(lista_de_orgaos)
            categoria_funcional = escolher_categoria()
            salario = verificar_numero(
                "SALARIO: R$ ",
                tipo_conversao=float,
                cor=Cor.CIANO,
                permitir_zero=True
            )

            novo_cadastro_funcionario = Funcionarios(
                nome, cpf, rg, nome_orgao, categoria_funcional, salario
            )

            self.nome_banco.inserir_funcionario_sql(novo_cadastro_funcionario)

            imprimir_cabecalho("DADOS SALVOS COM SUCESSO.")

            pausar()

            if continuar():
                continue
            else:
                return

    def alterar_funcionario(self):
        escolha_campos = {
            "1": "nome",
            "2": "cpf",
            "3": "rg",
            "4": "orgaos_emissores_id",
            "5": "salario",
            "6": "categoria_funcional"
        }

        while True:
            imprimir_cabecalho("CONSULTAR FUNCIONÁRIO", cor=Cor.LARANJA)

            consulta_id = enter_para_sair(
                "DIGITE ID DO FUNCIONÁRIO", cor=Cor.CIANO
            )

            if not consulta_id:
                return

            resultado_busca_funcionario = (
                self.nome_banco.consultar_funcionario_sql(consulta_id, "id")
            )
            resultado_busca_orgao = self.nome_banco.consultar_orgao_sql(
                resultado_busca_funcionario[6]
            )

            if not resultado_busca_funcionario:
                mostrar_erro("E03", Cor.AMARELO)
                continue

            imprimir_dados_na_tela(
                resultado_busca_funcionario, resultado_busca_orgao)

            print(f"{Cor.VERDE}CAMPOS DISPONÍVEIS PARA ALTERAÇÃO:")
            print(
                "[1] Nome   "
                "[2] CPF   "
                "[3] RG   "
                "[4] Órgão Emissor   "
                "[5] Salário   "
                "[6] Categoria"
                f"{Cor.RESET}"
            )

            imprimir_linha()

            print(
                f"{Cor.AMARELO}"
                f"Informe os números dos campos que deseja alterar "
                f"(separados por vírgula) "
                f"{Cor.RESET}"
            )
            opcoes_digitadas = enter_para_sair(
                "Digite os campos", Cor.AMARELO
            )

            imprimir_linha()

            if not opcoes_digitadas:
                return

            escolhas_separadas = opcoes_digitadas.split(",")

            print(f"{Cor.AMARELO}Digite os novos valores para: ")

            for opcao in escolhas_separadas:
                opcao = opcao.strip()
                nome_coluna = escolha_campos.get(opcao)
                if not nome_coluna:
                    print(
                        f"{Cor.AMARELO}"
                        f"⚠️   Campo {opcao} não localizado."
                        f"{Cor.RESET}"
                    )
                    continue

                if nome_coluna == "orgaos_emissores_id":
                    lista_de_orgaos = self.nome_banco.listar_orgaos_sql()
                    novo_valor = escolher_orgao_emissor(lista_de_orgaos)

                if nome_coluna == "salario":
                    novo_valor = verificar_numero(
                        f"[{nome_coluna.upper()}]: R$ ",
                        tipo_conversao=float,
                        cor=Cor.AZUL,
                        permitir_zero=True,
                    )
                elif nome_coluna == "categoria_funcional":
                    novo_valor = escolher_categoria()
                else:
                    novo_valor = verificar_vazio(
                        f"[{nome_coluna.upper()}]: ",
                        cor=Cor.AZUL
                    )

                self.nome_banco.alterar_funcionario_sql(
                    consulta_id, nome_coluna, novo_valor
                )

            imprimir_cabecalho(
                "Alterações realizadas com sucesso.", cor=Cor.MAGENTA
            )

            if continuar():
                continue
            else:
                return

    def consultar_funcionario(self):
        while True:
            imprimir_cabecalho("CONSULTAR FUNCIONÁRIO", cor=Cor.LARANJA)

            consulta_id = enter_para_sair(
                "DIGITE ID DO FUNCIONÁRIO", cor=Cor.CIANO
            )

            if not consulta_id:
                return

            resultado_busca_funcionario = (
                self.nome_banco.consultar_funcionario_sql(consulta_id, "id")
            )
            resultado_busca_orgao = self.nome_banco.consultar_orgao_sql(
                resultado_busca_funcionario[6]
            )

            if not resultado_busca_funcionario:
                mostrar_erro("E03", Cor.AMARELO)
                continue

            imprimir_dados_na_tela(
                resultado_busca_funcionario, resultado_busca_orgao
            )

            if continuar():
                continue
            else:
                return

    def excluir_funcionario(self):
        while True:
            imprimir_cabecalho("EXCLUSÃO DE FUNCIONÁRIO", cor=Cor.LARANJA)

            consulta_id = enter_para_sair(
                "DIGITE ID DO FUNCIONÁRIO", cor=Cor.CIANO
            )

            if not consulta_id:
                return

            resultado_busca = (
                self.nome_banco.consultar_funcionario_sql(consulta_id, "id")
            )

            if not resultado_busca:
                mostrar_erro("E03", Cor.AMARELO)
                continue

            imprimir_dados_na_tela(resultado_busca)

            print(
                f"{Cor.MAGENTA}"
                f"⚠️  ATENÇÃO: ESTE CADASTRO SERÁ EXCLUÍDO PERMANENTEMENTE!"
                f"{Cor.RESET}"
            )
            if continuar():
                self.nome_banco.excluir_funcionario_sql(consulta_id)
                imprimir_cabecalho(
                    "Cadastro excluído com sucesso", cor=Cor.AMARELO
                )
            else:
                return

    def iniciar_sistema(self):

        opcoes_menu = [
            "CADASTRAR ORGÃO EMISSOR",
            "CADASTRAR FUNCIONÁRIO",
            "ALTERAR FUNCIONÁRIO",
            "CONSULTAR FUNCIONÁRIO",
            "EXCLUIR FUNCIONÁRIO"
        ]

        escolha_menu = {
            1: self.cadastrar_orgao,
            2: self.cadastrar_funcionario,
            3: self.alterar_funcionario,
            4: self.consultar_funcionario,
            5: self.excluir_funcionario
        }

        while True:
            imprimir_cabecalho(
                "SISTEMA FAST-FOOD: CADASTRO DE FUNCIONÁRIOS",
                cor=Cor.LARANJA
            )

            criar_menu(opcoes_menu)

            opcao_digitada = verificar_numero(
                "Digite a opção desejada: ", int, permitir_zero=True)

            opcao_escolhida = escolha_menu.get(opcao_digitada)

            if opcao_escolhida:
                opcao_escolhida()
            elif opcao_digitada == 0:
                imprimir_cabecalho("SISTEMA SENDO ENCERRADO...", cor=Cor.VERDE)

                break
            else:
                mostrar_erro("E101", Cor.VERMELHO)


class OrgaoEmissor:
    def __init__(self, nome_orgao, id=None):
        self.id = id
        self.nome_orgao = nome_orgao

    def __str__(self):
        return f"ID: {self.id} - Orgão Emissor: {self.nome_orgao}"


if __name__ == "__main__":
    banco_fastfood = BancoDeDados(
        "localhost", "root", os.getenv("SENHA_BANCO"), "fastfood"
    )
    main = Sistema(banco_fastfood)
    main.iniciar_sistema()
