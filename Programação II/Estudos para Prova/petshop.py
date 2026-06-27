class Pet:
    def __init__(self, especie, raca, nome, idade):
        self._especie = especie
        self._raca = raca
        self._nome = nome
        self._idade = idade
        self._tutores = []
        self.atendimentos = []

    def __str__(self):
        return (
            ">>> Pet <<<\n"
            f"ESPÉCIE: {self._especie}\n"
            f"RAÇA: {self._raca}\n"
            f"NOME: {self._nome}\n"
            f"IDADE: {self._idade}"
        )

    def info_tutores(self):
        print(">>> Tutores <<<")
        for tutor in self._tutores:
            print(f"NOME TUTOR: {tutor._nome_completo}")

    def info_consultas(self):
        print(">>> Consultas <<<")
        for consulta in self.atendimentos:
            print(f"CONSULTA: {consulta.data}")
            print(f"VALOR: {consulta.valor}")


class Pessoa:
    def __init__(self, nome_completo, cpf, endereco, email):
        self._nome_completo = nome_completo
        self._cpf = cpf
        self._endereco = endereco
        self._email = email
        self._telefones = []

    def __str__(self):
        return (
            f"NOME: {self._nome_completo}\n"
            f"CPF: {self._cpf}\n"
            f"ENDEREÇO: {self._endereco}\n"
            f"E-MAIL: {self._email}"
        )

    def info_contato(self):
        print(">>> Contato <<<\n")
        for contador, telefone in enumerate(self._telefones, start=1):
            print(f"Telefone de contato[{contador}]: {telefone}")


class Tutor(Pessoa):
    def __init__(self, nome_completo, cpf, endereco, email):
        super().__init__(nome_completo, cpf, endereco, email)
        self._pets = []

    def __str__(self):
        return super().__str__()


class Veterinario(Pessoa):
    def __init__(self, nome_completo, cpf, endereco, email, crmv, turno):
        super().__init__(nome_completo, cpf, endereco, email)
        self.crmv = crmv
        self.turno = turno
        self.atendimentos = []

    def __str__(self):
        return (
            f">>> Veterinário <<<\n" +
            super().__str__() +
            f"\nCRMV: {self.crmv}\n"
            f"TURNO: {self.turno}"
        )

    def info_consultas(self):
        pass


class Consulta:
    def __init__(self, veterinario, paciente, acompanhante, valor, data):
        self.veterinario = veterinario
        self.paciente = paciente
        self.acompanhante = acompanhante
        self.valor = valor
        self.data = data

    def info_consulta(self):
        pass


def imprimir_linha():
    print(50 * "-")


if __name__ == "__main__":
    pessoa_01 = Pessoa("Jeferson Silveira", "89868927072",
                       "Rua Braga, 92", "jeferson@silveira.com")
    tutor_01 = Tutor("Pipe", "99999999", "Rua Braga, 92", "pipegamer@live.com")
    veterinario_01 = Veterinario("Edna", "90099877667", "Rua Braga, 92",
                                 "edna@veterinaria.com", "86986", "Manhã")
    pet_01 = Pet("Cachorro", "SRD", "Obsidiano", 1)
    consulta_01 = Consulta(veterinario_01, pet_01,
                           tutor_01, 200.00, "13/01/2026")

    pet_01.atendimentos.append(consulta_01)
    pet_01._tutores.append(tutor_01)

    tutor_01._pets.append(pet_01)
    tutor_01._telefones.append("51 98458-8888")

    veterinario_01.atendimentos.append(consulta_01)
    veterinario_01._telefones.append("51 98668-3284")

    pessoa_01._telefones.append("51 99999999")

    print(pessoa_01)
    imprimir_linha()
    print(tutor_01)
    tutor_01.info_contato()
    imprimir_linha()
    print(veterinario_01)
    veterinario_01.info_contato()
    imprimir_linha()
    print(pet_01)
    pet_01.info_tutores()
    pet_01.info_consultas()
