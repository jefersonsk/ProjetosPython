class Pessoa:
    def __init__(self, nome_completo, cpf, endereco, telefone, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def info(self):
        print(f"Nome: {self.nome_completo}")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereco}")
        print("Telefones: ")
        for dados in self.telefone:
            print(f"{dados}")
        print(f"E-mail: {self.email}")

    def contatos(self):
        print("=== CONTATOS ===")
        print(f"Nome: {self.nome_completo}")
        print("Telefones: ")
        for dados in self.telefone:
            print(f"{dados}")
        print(f"E-mail: {self.email}")


class Tutor(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, email):
        super().__init__(nome, cpf, endereco, telefone, email)
        self.pets = []

    def info(self):
        print("=== DADOS DO TUTOR ===")
        super().info()
        for dados in self.pets:
            print(f"Nome Pet: {dados.nome}")
            print(f"Espécie: {dados.especie}")
            print(f"Raça: {dados.raca}")


class Pet:
    def __init__(self, especie, raca, nome, idade):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.tutor = []

    def info(self):
        print("=== DADOS DO PET ===")
        print(f"Espécie: {self.especie}")
        print(f"Raça: {self.raca}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        for dados in self.tutor:
            print(f"Tutor: {dados.nome_completo}")


if __name__ == "__main__":
    tutor_01 = Tutor("José Silva", 8899009988, "Av. Um, 234",
                     ["51-88998888"], "123@gmail.com")
    pet_01 = Pet("Cachorro", "SRD", "Lobo", "4")
    pessoa_01 = Pessoa("Jeferson", 898888, "Rua Dois, 44",
                       ["51 33333333", "55 990099999"], "9999@hotmail.com")

    tutor_01.pets.append(pet_01)
    pet_01.tutor.append(tutor_01)

    pet_01.info()
    tutor_01.info()
    print("=== DADOS PESSOA ===")
    pessoa_01.info()
    pessoa_01.contatos()
