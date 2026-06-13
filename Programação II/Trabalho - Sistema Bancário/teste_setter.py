class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo_centavos / 100

    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self._saldo_centavos = int(valor * 100)
        else:
            print("valor inválido")

    def deposito(self, valor):
        self.saldo += valor


conta01 = ContaBancaria("Jeferson", 100)

print(f"O correntista {conta01.nome} tem saldo de R$ {conta01.saldo:.2f}")

conta01.deposito(-100)

print(f"Saldo: R$ {conta01.saldo:.2f}")
