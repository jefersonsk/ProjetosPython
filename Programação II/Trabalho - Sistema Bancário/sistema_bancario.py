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
        self.saldo = saldo
        self._senha = senha

    @property
    def saldo(self):
        return self._saldo_centavos / 100

    @saldo.setter
    def saldo(self, valor_em_reais):
        self._saldo_centavos = int(valor_em_reais * 100)

    def saque(self, valor_em_reais):
        valor_convertido_centavos = int(valor_em_reais * 100)
        if self._saldo_centavos < valor_convertido_centavos:
            print("Saldo Insuficiente.")
        else:
            self._saldo_centavos -= valor_convertido_centavos

    def deposito(self, valor_em_reais):
        valor_convertido_centavos = int(valor_em_reais * 100)
        self._saldo_centavos += valor_convertido_centavos

    def verifica_senha(self, senha):
        return self._senha == senha

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
        print(f"🏦 Banco: {self._banco}")
        print(f"🔢 Conta: {self._numero_conta}")
        print(f"👤 Titular: {self._titular}")
        print(f"💰 Saldo: R$ {self.saldo:.2f}")
        print(f"📉 Taxas Mensais: R$ {self.__taxas_mensais:.2f}")

    def novo_mes(self):
        taxa_convertida_centavos = int(self.__taxas_mensais * 100)
        self._saldo_centavos -= taxa_convertida_centavos


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

    def info(self):
        print(f"🏦 Banco: {self._banco}")
        print(f"🔢 Conta: {self._numero_conta}")
        print(f"👤 Titular: {self._titular}")
        print(f"💰 Saldo: R$ {self.saldo:.2f}")
        print(f"📈 Rendimento: {self.__rendimento} %")

    def novo_mes(self):
        self._saldo_centavos += int(
            (self._saldo_centavos * self.__rendimento) / 100
        )
        self.__quantidade_saques = self.__saques_mensais

    def saque(self, valor):
        if self.__quantidade_saques > 0:
            super().saque(valor)

            self.__quantidade_saques -= 1
        else:
            print("Limite de saques excedidos.")


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

    def info(self):
        print(f"NOME: {self.nome}")
        print(f"SOBRENOME: {self.sobrenome}")
        print(f"CPF: {self.__cpf}")
        print(f"IDADE: {self.idade}")

    def info_contas(self):
        for conta in self.__contas_bancarias:
            conta.info()

    @classmethod
    def criar_pessoa_pelo_teclado(cls):
        nome = input("NOME: ")
        sobrenome = input("SOBRENOME: ")
        cpf = input("CPF: ")
        idade = input("IDADE: ")

        return cls(nome, sobrenome, cpf, idade)


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

    def criar_conta(self, conta):
        self.__contas_bancarias.append(conta)

    def fechar_conta(self, conta):
        self.__contas_bancarias.remove(conta)


cliente01 = ContaCorrente("Jeferson", "Brasil", "0001-1", 500.50, "xyz", 5)

cliente01.info()
