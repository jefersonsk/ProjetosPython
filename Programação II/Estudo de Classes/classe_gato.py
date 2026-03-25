AZUL = "\033[34m"
RESET = "\033[0m"

class Gato:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Aqui entra o método mágico!
    def __str__(self):
        # Em vez de vários prints, retornamos um único grande bloco de texto
        return f"""{AZUL}--- Ficha do Gato ---{RESET}
                    Nome: {self.nome}
                    Idade: {self.idade} anos"""

# Quando criamos o objeto e usamos o print nativo do Python:
meu_gato = Gato("Frajola", 3)
print(meu_gato)