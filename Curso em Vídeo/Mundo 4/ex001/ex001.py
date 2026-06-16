class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    # Método de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
g1 = Gafanhoto()
g1.nome  = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Jeferson"
g2.idade = 50
print(g2.mensagem())

