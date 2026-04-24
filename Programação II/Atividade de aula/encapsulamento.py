class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")

    def mostra_saldo(self):
        print(f"Saldo atual de {self.titular}: R$ {self.__saldo}")


if __name__ == "__main__":
    minha_conta = ContaBancaria("Jeferson", 1000)

    minha_conta.depositar(500)
    minha_conta.mostra_saldo()
