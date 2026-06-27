import json
import getpass
from abc import ABC, abstractmethod
from utilidades import Cor
from utilidades import (
    verificar_numero,
    verificar_vazio,
    criar_menu,
    imprimir_cabecalho,
    imprimir_linha,
    pausar,
    continuar,
    mostrar_erro,
    validar_cpf,
    validar_cnpj,
    formatar_cpf,
    formatar_cnpj
)


TAXA_MENSAL = 15.0
RENDIMENTO_POUPANCA = 0.5
SAQUES_PERMITIDOS = 3


class ContaBancaria(ABC):
    def __init__(
        self,
        titular,
        banco,
        numero_conta,
        saldo,
        senha
    ):
        self._titular = titular
        self._banco = banco
        self._numero_conta = numero_conta
        self.saldo = saldo
        self._senha = senha

    def exportar_dicionario(self):
        return {
            "titular": self._titular.cpf,
            "banco": self._banco.numero_banco,
            "numero_conta": self._numero_conta,
            "saldo": self.saldo,
            "senha": self._senha
        }

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo_centavos / 100

    @saldo.setter
    def saldo(self, valor_em_reais):
        self._saldo_centavos = int(valor_em_reais * 100)

    def saque(self, valor_em_reais=None):
        if not self.verifica_senha():
            return

        print(
            f"{Cor.VERDE}Saldo da conta: "
            f"{Cor.AZUL}R$ {self.saldo:.2f}{Cor.RESET}"
        )

        while True:
            if valor_em_reais is None:
                valor_em_reais = verificar_numero(
                    "Digite o Valor [Enter para SAIR]: R$ ",
                    tipo_conversao=float,
                    cor=Cor.VERDE,
                    permitir_vazio=True
                )

            if valor_em_reais is None:
                return False

            if valor_em_reais <= 0:
                mostrar_erro("E01", cor=Cor.AMARELO)
                valor_em_reais = None
                continue

            valor_convertido_centavos = int(valor_em_reais * 100)

            if self._saldo_centavos < valor_convertido_centavos:
                mostrar_erro("E02", cor=Cor.AMARELO)
                valor_em_reais = None
                continue
            else:
                self._saldo_centavos -= valor_convertido_centavos
                return True

    def deposito(self, valor_em_reais=None):
        print(
            f"{Cor.VERDE}Saldo da conta: "
            f"{Cor.AZUL}R$ {self.saldo:.2f}{Cor.RESET}"
        )

        if valor_em_reais is None:
            valor_em_reais = verificar_numero(
                "Digite o Valor: R$ ",
                tipo_conversao=float,
                cor=Cor.VERDE,
                permitir_vazio=True
            )

        if valor_em_reais is None:
            return False

        if valor_em_reais <= 0:
            mostrar_erro("E03")
            return

        valor_convertido_centavos = int(valor_em_reais * 100)

        self._saldo_centavos += valor_convertido_centavos
        return True

    def verifica_senha(self, senha=None):
        while True:
            senha = None
            if senha is None:
                senha = getpass.getpass(
                    f"{Cor.VERDE}Digite sua senha: {Cor.RESET}"
                )

            if self._senha != senha:
                mostrar_erro("E04", cor=Cor.AMARELO)
                continue

            return True

    @abstractmethod
    def novo_mes(self):
        pass


class ContaCorrente(ContaBancaria):
    def __init__(
        self,
        titular,
        banco,
        numero_conta,
        saldo,
        senha,
        taxas_mensais
    ):
        super().__init__(titular, banco, numero_conta, saldo, senha)
        self.__taxas_mensais = taxas_mensais

    def __str__(self):
        return (
            f"🏦 Banco: {self._banco.nome_banco}\n"
            f"🔢 Conta: {self._numero_conta:06} - Conta Corrente\n"
            f"👤 Titular: {self._titular.nome} {self._titular.sobrenome}\n"
            f"🪪  CPF: {formatar_cpf(self._titular.cpf)}\n"
            f"💰 Saldo: R$ {self.saldo:.2f}\n"
            f"📉 Taxas Mensais: R$ {self.__taxas_mensais:.2f}"
        )

    def novo_mes(self):
        taxa_convertida_centavos = int(self.__taxas_mensais * 100)
        self._saldo_centavos -= taxa_convertida_centavos

    def exportar_dicionario(self):
        dados = super().exportar_dicionario()
        dados["tipo"] = "conta_corrente"
        dados["taxas_mensais"] = self.__taxas_mensais
        return dados

    @classmethod
    def importar_dados_json(cls, dados, objeto_titular, objeto_banco):
        numero_conta = dados["numero_conta"]
        saldo = dados["saldo"]
        senha = dados["senha"]
        taxas_mensais = dados["taxas_mensais"]

        return cls(
            objeto_titular,
            objeto_banco,
            numero_conta,
            saldo,
            senha,
            taxas_mensais
        )

    @classmethod
    def criar_conta_corrente(
        cls, titular_encontrado,
        banco_escolhido,
        numero_gerado
    ):
        titular = titular_encontrado
        banco = banco_escolhido
        numero_conta = numero_gerado
        saldo = verificar_numero(
            "SALDO INICIAL: R$ ", tipo_conversao=float, cor=Cor.VERDE
        )
        senha = getpass.getpass(
            f"{Cor.VERDE}Digite sua senha: {Cor.RESET}"
        )
        # senha = verificar_vazio("SENHA: ", cor=Cor.VERDE)
        taxas_mensais = TAXA_MENSAL

        return cls(titular, banco, numero_conta, saldo, senha, taxas_mensais)


class ContaPoupanca(ContaBancaria):
    def __init__(
        self,
        titular,
        banco,
        numero_conta,
        saldo,
        senha,
        rendimento,
        saques_mensais
    ):
        super().__init__(titular, banco, numero_conta, saldo, senha)
        self.__rendimento = rendimento
        self.__quantidade_saques = saques_mensais
        self.__saques_mensais = saques_mensais

    def __str__(self):
        return (
            f"🏦 Banco: {self._banco.nome_banco}\n"
            f"🔢 Conta: {self._numero_conta:06} - Conta Poupança\n"
            f"👤 Titular: {self._titular.nome} {self._titular.sobrenome}\n"
            f"🪪  CPF: {formatar_cpf(self._titular.cpf)}\n"
            f"💰 Saldo: R$ {self.saldo:.2f}\n"
            f"📈 Rendimento: {self.__rendimento} %\n"
            f"🎟️ Saques Mensais: {self.__quantidade_saques}"
        )

    def novo_mes(self):
        self._saldo_centavos += int(
            (self._saldo_centavos * self.__rendimento) / 100
        )
        self.__quantidade_saques = self.__saques_mensais

    def saque(self, valor_em_reais=None):
        if self.__quantidade_saques > 0:
            super().saque(valor_em_reais)

            self.__quantidade_saques -= 1
        else:
            mostrar_erro("E05", cor=Cor.AMARELO)

    def exportar_dicionario(self):
        dados = super().exportar_dicionario()
        dados["tipo"] = "conta_poupanca"
        dados["rendimentos"] = self.__rendimento
        dados["quantidade_saque"] = self.__quantidade_saques
        dados["saques_mensais"] = self.__saques_mensais
        return dados

    @classmethod
    def importar_dados_json(cls, dados, objeto_titular, objeto_banco):
        numero_conta = dados["numero_conta"]
        saldo = dados["saldo"]
        senha = dados["senha"]
        rendimentos = dados["rendimentos"]
        saques_mensais = dados["saques_mensais"]

        qtd_restante = dados["quantidade_saque"]
        conta_recuperada = cls(
            objeto_titular,
            objeto_banco,
            numero_conta,
            saldo,
            senha,
            rendimentos,
            saques_mensais
        )
        conta_recuperada._ContaPoupanca__quantidade_saques = qtd_restante

        return conta_recuperada

    @classmethod
    def criar_conta_poupanca(
        cls, titular_encontrado,
        banco_escolhido,
        numero_gerado
    ):
        titular = titular_encontrado
        banco = banco_escolhido
        numero_conta = numero_gerado
        saldo = verificar_numero(
            "SALDO INICIAL: R$ ", tipo_conversao=float, cor=Cor.VERDE
        )
        senha = verificar_vazio("SENHA: ", cor=Cor.VERDE)
        rendimentos = RENDIMENTO_POUPANCA
        saques_mensais = SAQUES_PERMITIDOS

        return cls(
            titular,
            banco,
            numero_conta,
            saldo,
            senha,
            rendimentos,
            saques_mensais
        )


class Pessoa:
    def __init__(
        self,
        nome,
        sobrenome,
        cpf,
        idade
    ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self.idade = idade
        self.__contas_bancarias = []

    def __str__(self):
        linha = "-" * 80
        cpf_visual = formatar_cpf(self.__cpf)

        return (
            f"👤 Titular: {self.nome} {self.sobrenome}\n"
            f"🪪  CPF: {cpf_visual}\n"
            f"📅 Idade: {self.idade} Anos"
        )

        return (
            f"{linha}\n"
            f"{Cor.AZUL}NOME: {Cor.AMARELO}"
            f"{self.nome:<15} "
            f"{Cor.AZUL}SOBRENOME: {Cor.AMARELO}"
            f"{self.sobrenome:<30}\n"
            f"{Cor.AZUL}CPF: {Cor.AMARELO}"
            f"{cpf_visual:<15} "
            f"{Cor.AZUL}IDADE: {Cor.AMARELO}"
            f"{self.idade:<31}\n{Cor.RESET}"
            f"{linha}"
        )

    def info_contas(self):
        for conta in self.__contas_bancarias:
            print(conta)

    def adicionar_conta(self, conta):
        self.__contas_bancarias.append(conta)

    @property
    def contas_bancarias(self):
        return self.__contas_bancarias

    @property
    def cpf(self):
        return self.__cpf

    @classmethod
    def criar_pessoa(cls, lista_pessoas):
        while True:
            cpf = validar_cpf("CPF: ", cor=Cor.VERDE)

            if not cpf:
                return

            cpf_repetido = False

            for pessoa in lista_pessoas:
                if cpf == pessoa.cpf:
                    cpf_repetido = True
                    mostrar_erro("E08", cor=Cor.AMARELO)
                    break

            if not cpf_repetido:
                break

        nome = verificar_vazio("NOME: ", cor=Cor.VERDE)
        sobrenome = verificar_vazio("SOBRENOME: ", cor=Cor.VERDE)
        idade = verificar_numero(
            "IDADE: ", tipo_conversao=int, cor=Cor.VERDE)

        imprimir_cabecalho(
            "✅  Cliente cadastrado com sucesso.", cor=Cor.CIANO
        )

        return cls(nome, sobrenome, cpf, idade)

    def exportar_dicionario(self):
        contas_convertidas = []
        for conta in self.__contas_bancarias:
            contas_convertidas.append(conta.exportar_dicionario())

        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cpf": self.__cpf,
            "idade": self.idade,
            "contas": contas_convertidas
        }

    @classmethod
    def importar_dados_json(cls, dados, lista_bancos):
        nome = dados["nome"]
        sobrenome = dados["sobrenome"]
        cpf = dados["cpf"]
        idade = dados["idade"]

        nova_pessoa = cls(nome, sobrenome, cpf, idade)

        for dados_da_conta in dados["contas"]:
            banco_da_conta = None
            numero_procurado = dados_da_conta["banco"]

            for banco in lista_bancos:
                if banco.numero_banco == numero_procurado:
                    banco_da_conta = banco

            if dados_da_conta["tipo"] == "conta_corrente":
                nova_conta = (
                    ContaCorrente.importar_dados_json(
                        dados_da_conta,
                        nova_pessoa,
                        banco_da_conta
                    )
                )
            else:
                nova_conta = (
                    ContaPoupanca.importar_dados_json(
                        dados_da_conta,
                        nova_pessoa,
                        banco_da_conta
                    )
                )

            nova_pessoa.adicionar_conta(nova_conta)
            banco_da_conta.criar_conta(nova_conta)

        return nova_pessoa


class Banco:
    def __init__(
        self,
        nome_banco,
        cnpj,
        numero_banco
    ):
        self.__nome_banco = nome_banco
        self.__cnpj = cnpj
        self.__numero_banco = numero_banco
        self.__contas_bancarias = []

    def __str__(self):
        cnpj_visual = formatar_cnpj(self.__cnpj)

        return (
            f"🏦 Banco: {self.__nome_banco}\n"
            f"🆔 Número Banco: {self.__numero_banco}\n"
            f"📜 CNPJ: {cnpj_visual}\n"
        )

    def criar_conta(self, conta):
        self.__contas_bancarias.append(conta)

    def fechar_conta(self, conta):
        self.__contas_bancarias.remove(conta)

    @property
    def numero_banco(self):
        return self.__numero_banco

    @property
    def contas_bancarias(self):
        return self.__contas_bancarias

    @property
    def nome_banco(self):
        return self.__nome_banco

    @property
    def cnpj(self):
        return self.__cnpj

    @classmethod
    def criar_banco(cls, lista_bancos):
        while True:
            cnpj = validar_cnpj("CNPJ: ", cor=Cor.VERDE)

            if not cnpj:
                return

            cnpj_repetido = False

            for banco in lista_bancos:
                if cnpj == banco.cnpj:
                    cnpj_repetido = True
                    mostrar_erro("E10", cor=Cor.AMARELO)
                    break

            if not cnpj_repetido:
                break

        nome_banco = verificar_vazio("NOME DO BANCO: ", cor=Cor.VERDE)

        if not nome_banco:
            return

        numero_banco = len(lista_bancos) + 1

        imprimir_cabecalho("✅ Banco cadastrado com sucesso.", cor=Cor.CIANO)

        return cls(nome_banco, cnpj, numero_banco)

    def exportar_dicionario(self):
        return {
            "nome_do_banco": self.__nome_banco,
            "cnpj": self.__cnpj,
            "numero_do_banco": self.__numero_banco
        }

    @classmethod
    def importar_dados_json(cls, dados):
        nome_banco = dados["nome_do_banco"]
        cnpj = dados["cnpj"]
        numero_banco = dados["numero_do_banco"]

        return cls(nome_banco, cnpj, numero_banco)


def escolher_banco(lista_bancos) -> Banco:
    lista_ids_bancos = []

    imprimir_cabecalho("ESCOLHA O BANCO:", cor=Cor.AMARELO)

    for banco in lista_bancos:
        print(
            f"{Cor.CIANO_CLARO}"
            f"[{banco.numero_banco}]: {banco.nome_banco} - "
            f"CNPJ: {formatar_cnpj(banco.cnpj)}"
            f"{Cor.RESET}"
        )
        lista_ids_bancos.append(banco.numero_banco)

    imprimir_linha()

    while True:
        escolha_banco = verificar_numero(
            "\nNUMERO BANCO: ",
            tipo_conversao=int,
            cor=Cor.VERDE
        )

        if escolha_banco in lista_ids_bancos:
            for banco in lista_bancos:
                if banco.numero_banco == escolha_banco:
                    return banco
        else:
            mostrar_erro("E101", cor=Cor.AMARELO)


def salvar_dados_json(lista_bancos: list, lista_pessoas: list):
    dados_gerais = {
        "bancos": [],
        "pessoas": [],
    }

    for banco in lista_bancos:
        dados_gerais["bancos"].append(banco.exportar_dicionario())

    for pessoa in lista_pessoas:
        dados_gerais["pessoas"].append(pessoa.exportar_dicionario())

    with open("banco_de_dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_gerais, arquivo, indent=4, ensure_ascii=False)

    print("✅ Dados salvos com sucesso no arquivo 'banco_de_dados.json'!")


def carregar_dados():
    try:
        with open("banco_de_dados.json", "r", encoding="utf-8") as arquivo:
            dados_gerais = json.load(arquivo)

        bancos_carregados = []
        pessoas_carregadas = []

        for dados in dados_gerais["bancos"]:
            bancos_carregados.append(
                Banco.importar_dados_json(dados)
            )

        for dados in dados_gerais["pessoas"]:
            pessoas_carregadas.append(
                Pessoa.importar_dados_json(dados, bancos_carregados)
            )

        return bancos_carregados, pessoas_carregadas

    except FileNotFoundError:
        print("⚠️ Arquivo não encontrado. Iniciando sistema vazio.")
        return [], []


def cadastrar_banco(lista_bancos: list, lista_pessoas: list):
    while True:
        imprimir_cabecalho("CADASTRO DE BANCO", cor=Cor.LARANJA)

        novo = Banco.criar_banco(lista_bancos)

        if novo is None:
            return

        lista_bancos.append(novo)

        if not continuar():
            return


def cadastrar_pessoa(lista_bancos: list, lista_pessoas: list):
    while True:
        imprimir_cabecalho("CADASTRO DE CLIENTES", cor=Cor.LARANJA)

        novo = Pessoa.criar_pessoa(lista_pessoas)

        if novo is None:
            return

        lista_pessoas.append(novo)

        if not continuar():
            return


def localizar_pessoa(lista_pessoas: list):
    while True:
        cpf_digitado = validar_cpf("CPF", cor=Cor.VERDE)

        if not cpf_digitado:
            return

        cliente_encontrado = None

        for pessoa in lista_pessoas:
            if pessoa.cpf == cpf_digitado:
                cliente_encontrado = pessoa
                return pessoa

        mostrar_erro("E06", cor=Cor.AMARELO)

        if not continuar():
            return None


def criar_conta_pessoa(lista_bancos: list, lista_pessoas: list):
    opcao_menu = [
        "CONTA CORRENTE",
        "CONTA POUPANÇA"
    ]

    while True:
        imprimir_cabecalho("CRIAR CONTA", cor=Cor.AMARELO)

        cliente_encontrado = localizar_pessoa(lista_pessoas)

        if cliente_encontrado is None:
            return

        print(cliente_encontrado)

        banco_escolhido = escolher_banco(lista_bancos)
        numero_conta_gerada = len(banco_escolhido.contas_bancarias) + 1

        imprimir_cabecalho("ESCOLHA O TIPO DE CONTA:")

        criar_menu(opcao_menu, tipo="submenu")

        opcao_escolhida = verificar_numero(
            "Digite a opção desejada: ",
            tipo_conversao=int,
            cor=Cor.AMARELO,
            permitir_zero=True
        )

        if opcao_escolhida == 1:
            nova_conta = ContaCorrente.criar_conta_corrente(
                cliente_encontrado,
                banco_escolhido,
                numero_conta_gerada
            )
        elif opcao_escolhida == 2:
            nova_conta = ContaPoupanca.criar_conta_poupanca(
                cliente_encontrado,
                banco_escolhido,
                numero_conta_gerada
            )
        elif opcao_escolhida == 0:
            return
        else:
            mostrar_erro("E101", cor=Cor.AMARELO)
            continue

        cliente_encontrado.adicionar_conta(nova_conta)
        banco_escolhido.criar_conta(nova_conta)

        imprimir_cabecalho("✅ Conta Criada com sucesso.", cor=Cor.CIANO)

        print(nova_conta)
        imprimir_linha()

        if not continuar():
            return


def efetuar_deposito(lista_bancos: list, lista_pessoas: list):
    while True:
        imprimir_cabecalho("EFETUAR DEPÓSITO", cor=Cor.LARANJA)

        cliente_encontrado = localizar_pessoa(lista_pessoas)

        if cliente_encontrado is None:
            return

        contas = cliente_encontrado.contas_bancarias

        imprimir_cabecalho(
            f"Contas cadastradas para "
            f"{Cor.MAGENTA}"
            f"{cliente_encontrado.nome} {cliente_encontrado.sobrenome}:"
            f"{Cor.RESET}",
            cor=Cor.AMARELO
        )

        mostrar_contas(contas)

        escolher_conta = verificar_numero(
            "Escolha a conta desejada: ",
            tipo_conversao=int,
            cor=Cor.VERDE
        )

        if 1 <= escolher_conta <= len(contas):
            conta_escolhida = contas[escolher_conta - 1]
            resultado_operacao = conta_escolhida.deposito()

            if not resultado_operacao:
                return
        else:
            mostrar_erro("E101", cor=Cor.AMARELO)

        imprimir_cabecalho("✅ Depósito efetuado com sucesso.")

        if not continuar():
            return


def mostrar_contas(lista_contas: list):
    for numero, dados in enumerate(lista_contas, start=1):
        tipo_conta = type(dados).__name__
        print(
            f"{Cor.CIANO_CLARO}"
            f"[{numero}] Conta: {dados.numero_conta:06} - "
            f"Tipo: {tipo_conta} - "
            f"Banco: {dados._banco.nome_banco}"
            f"{Cor.RESET}"
        )

    imprimir_linha()


def efetuar_saque(lista_bancos: list, lista_pessoas: list):
    while True:
        imprimir_cabecalho("EFETUAR SAQUE", cor=Cor.LARANJA)

        cliente_encontrado = localizar_pessoa(lista_pessoas)

        if cliente_encontrado is None:
            return

        contas = cliente_encontrado.contas_bancarias

        imprimir_cabecalho(
            f"Contas cadastradas para "
            f"{Cor.MAGENTA}"
            f"{cliente_encontrado.nome} {cliente_encontrado.sobrenome}:"
            f"{Cor.RESET}",
            cor=Cor.AMARELO
        )

        mostrar_contas(contas)

        escolher_conta = verificar_numero(
            "Escolha a conta desejada: ",
            tipo_conversao=int,
            cor=Cor.VERDE
        )

        if 1 <= escolher_conta <= len(contas):
            conta_escolhida = contas[escolher_conta - 1]
            resultado_operacao = conta_escolhida.saque()

            if not resultado_operacao:
                return
        else:
            mostrar_erro("E101", cor=Cor.AMARELO)

        imprimir_cabecalho("✅ Saque efetuado com sucesso.")

        if not continuar():
            return


def mudar_de_mes(lista_bancos: list, lista_pessoas: list):
    imprimir_cabecalho("NOVO MÊS", cor=Cor.LARANJA)

    for pessoa in lista_pessoas:
        for conta in pessoa.contas_bancarias:
            conta.novo_mes()

    imprimir_cabecalho("✅ Taxas e Rendimentos aplicados em todas as contas.")

    if not continuar():
        return


def exibir_relatorio_contas(lista_bancos: list, lista_pessoas: list):
    imprimir_cabecalho("RELATÓRIO DE CONTAS", cor=Cor.LARANJA)

    for pessoa in lista_pessoas:
        for conta in pessoa.contas_bancarias:
            print(conta)
            imprimir_linha()

    pausar()


def exibir_relatorio_bancos(lista_bancos: list, lista_pessoas: list):
    imprimir_cabecalho("RELATÓRIO DE BANCOS", cor=Cor.LARANJA)

    for banco in lista_bancos:
        print(banco)
        imprimir_linha()

    pausar()


def encerrar_conta(lista_bancos: list, lista_pessoas: list):
    while True:
        imprimir_cabecalho("ENCERRAMENTO DE CONTA", cor=Cor.LARANJA)
        cliente_encontrado = localizar_pessoa(lista_pessoas)

        if cliente_encontrado is None:
            return

        print(cliente_encontrado)

        contas = cliente_encontrado.contas_bancarias

        mostrar_contas(contas)

        escolher_conta = verificar_numero(
            "Escolha a conta desejada: ",
            tipo_conversao=int,
            cor=Cor.VERDE
        )

        if 1 <= escolher_conta <= len(contas):
            conta_escolhida = contas[escolher_conta - 1]

            imprimir_linha()
            print(conta_escolhida)

            if conta_escolhida.saldo > 0:
                imprimir_cabecalho(
                    "⚠️ Conta com saldo positivo. "
                    "Efetue o saque antes de encerrar.",
                    cor=Cor.AMARELO
                )
            elif conta_escolhida.saldo < 0:
                imprimir_cabecalho(
                    "⚠️ Conta com saldo negativo. "
                    "Quite as dívidas antes de encerrar.",
                    cor=Cor.AMARELO
                )
            else:
                contas.remove(conta_escolhida)
                conta_escolhida._banco.fechar_conta(conta_escolhida)

                imprimir_cabecalho(
                    "✅ Conta encerrada com sucesso!", cor=Cor.CIANO
                )

            if not continuar():
                return

        else:
            mostrar_erro("E101", cor=Cor.AMARELO)


def main():
    opcoes_menu = [
        "CADASTRAR BANCO",
        "CADASTRAR PESSOA",
        "CRIAR CONTA",
        "EFETUAR SAQUE",
        "EFETUAR DEPÓSITO",
        "RELATÓRIO DE CONTAS",
        "RELATÓRIO DE BANCOS",
        "ENCERRAR CONTA",
        "NOVO MÊS"
    ]

    escolha_menu = {
        1: cadastrar_banco,
        2: cadastrar_pessoa,
        3: criar_conta_pessoa,
        4: efetuar_saque,
        5: efetuar_deposito,
        6: exibir_relatorio_contas,
        7: exibir_relatorio_bancos,
        8: encerrar_conta,
        9: mudar_de_mes
    }

    meus_bancos, meus_clientes = carregar_dados()

    while True:
        imprimir_cabecalho("SISTEMA BANCÁRIO", cor=Cor.LARANJA)

        criar_menu(opcoes_menu)

        opcao_digitada = verificar_numero(
            "Digite a opção desejada: ", int, permitir_zero=True
        )

        opcao_escolhida = escolha_menu.get(opcao_digitada)

        if opcao_escolhida:
            opcao_escolhida(meus_bancos, meus_clientes)
        elif opcao_digitada == 0:
            imprimir_cabecalho("SISTEMA SENDO ENCERRADO...", cor=Cor.VERDE)
            salvar_dados_json(meus_bancos, meus_clientes)
            break
        else:
            mostrar_erro("E101", Cor.VERMELHO)


if __name__ == "__main__":
    main()
