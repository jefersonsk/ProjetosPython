class Pessoa:
    def __init__(self, nome, sobrenome, sexo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo

    def apresentar(self):
        print(self.nome, self.sobrenome)

lista_pessoas = []

# Coletando os dados
while True:
    nome_digitado = input("Digite o nome (ou 'sair' para parar): ")
    
    if nome_digitado.lower() == 'sair':
        break
        
    sobrenome_digitado = input("Digite o sobrenome: ")
    sexo_digitado = input("Digite o sexo: ")
    
    # Criando o objeto e guardando na lista
    nova_pessoa = Pessoa(nome=nome_digitado, sobrenome=sobrenome_digitado, sexo=sexo_digitado)
    lista_pessoas.append(nova_pessoa)

# Exibindo os resultados usando o método do próprio objeto
print("\n--- Pessoas Cadastradas ---")
for x in lista_pessoas:
    x.apresentar()
        