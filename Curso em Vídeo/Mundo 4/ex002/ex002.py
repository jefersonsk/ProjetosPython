class Gafanhoto:
    """
    Essa Classe cria um Gafanhoto que tem nome e idade

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome="Vazio", idade=0):
        self.nome = nome
        self.idade = idade

    # Método de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado; nome = {self.nome}; idade = {self.idade}"
    
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Jeferson", 50)
print(g2)

g3 = Gafanhoto()
print(g3)

# Dunder Atributtes 
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
print(g1.__doc__) # Mostra a documentação do objeto.