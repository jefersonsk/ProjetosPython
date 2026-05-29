from abc import ABC, abstractmethod


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
        self._saldo = saldo
        self._senha = senha

    def saque(self, valor):
        pass

    def deposito(self, valor):
        pass

    def verifica_senha(self, senha):
        pass

    @abstractmethod
    def info(self):
        pass

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

    def info(self):
        pass

    def novo_mes(self):
        self._saldo -= self.__taxas_mensais


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
        self.__saques_mensais = saques_mensais


class Pessoa:
    def __init__(
        self,
        nome,
        sobrenome,
        idade,
        cpf
    ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.__cpf = cpf
        self.__contas_bancarias = []

    def info(self):
        pass

    def info_contas(self):
        pass
