class ContaBancaria:
    """
        Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

        print(f"Conta {self.id} criada com sucesso!")
        print(f"Saldo da conta: R$ {self.saldo:.2f}")

    def __str__(self):
        return (
            f"A conta {self.id} de {self.titular} "
            f"tem R$ {self.saldo:.2f} de saldo."
        )
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} autorizado na conta {self.id}")

    def saque(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R$ {valor:.2f} na conta {self.id}")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} autorizado na conta {self.id}")

c1 = ContaBancaria(112, "Jeferson", 3000)

c1.depositar(500)

print(c1)

c1.saque(10000)

print(c1)

# print(c1.__doc__)