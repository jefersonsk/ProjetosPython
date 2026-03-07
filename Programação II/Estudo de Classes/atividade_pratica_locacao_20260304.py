class Locacao:
    def __init__(self, placa_carro, cpf_cliente, data_retirada, data_entrega, valor_servico):
        self.placa_carro = placa_carro
        self.cpf_cliente = cpf_cliente
        self.data_retirada = data_retirada
        self.data_entrega = data_entrega
        self.valor_servico = valor_servico


def criar_menu(lista: list)  -> None:
    """
    Criar menu de opções.

    Args:
        lista (list): Lista de opções que devem ser adicionadas ao menu.
    """
    contador = 1

    for item in lista:
        print(f"{contador} - {item}")
        contador += 1
    criar_linha("-")

def criar_linha(caracter: str, tamanho = 50) -> str:
    """
    Cria uma linha com o caracter escolhido.

    Args:
        caracter (str): Caracter que será usado para criar a linha.
        tamanho (int, optional): Quantidade de caracteres que irá formar a linha. Como default o valor é 50.

    Returns:
        str: _description_
    """
    return print(caracter * tamanho)

def criar_cabecalho(mensagem: str, tamanho: int) -> None:
    criar_linha("-")
    print(mensagem.center(tamanho))
    criar_linha("-")

criar_cabecalho("SISTEMA DE LOCAÇÃO DE VEÍCULOS", 50)
criar_menu(["CADASTRO DE LOCAÇÃO", "LISTAGEM DE LOCAÇÕES", "BUSCA DE LOCAÇÃO POR PLACA DO VEÍCULO", ""
"BUSCA DE LOCAÇÃO POR CPF DO CLIENTE", "FECHAR PROGRAMA"])