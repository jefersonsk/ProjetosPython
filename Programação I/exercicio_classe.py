class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["Basic", "Premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print("Plano Inválido")


cliente = Cliente("Jeferson da Silveira Kendzierski", "ujh@com", "Intermediário")
print(cliente.nome)