QUANTIDADE_POR_PESSOA = 400 / 1000  # Convertido para gramas
PRECO_POR_QUILO = 82.40


class Churrasco:
    def __init__(self, titulo_evento, quantidade_pessoas):
        self.titulo_evento = titulo_evento
        self.quantidade_pessoas = quantidade_pessoas

    def analisar(self):
        quantidade_total = QUANTIDADE_POR_PESSOA * self.quantidade_pessoas
        valor_total = quantidade_total * PRECO_POR_QUILO
        valor_por_pessoa = valor_total / self.quantidade_pessoas

        print(
            f"Analisando o {self.titulo_evento} com "
            f"{self.quantidade_pessoas} pessoas:"
        )
        print(f"Recomendo comprar {quantidade_total} Kg de carne.")
        print(f"O custo total será de R$ {valor_total:.2f}.")
        print(f"Cada pessoa pagará R$ {valor_por_pessoa:.2f}")


if __name__ == "__main__":
    evento_01 = Churrasco("Churras da Galera", 15)

    evento_01.analisar()
