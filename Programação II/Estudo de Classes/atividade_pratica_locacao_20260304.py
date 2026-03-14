from datetime import datetime

MENSAGEM_ERRO = {"E01": "ERRO: Opção digitada não é um valor númerico.",
                 "E02": "ERRO: Data de retirada anterior a data de entrega.",
                 "E03": "ERRO: Data inválida.",
                 "E04": "ERRO: Nenhum dado cadastrado.",
                 "E05": "ERRO: Placa não cadastrada.",
                 "E06": "ERRO: CPF não cadastrado.",
                 "E07": "ERRO: Opção inválida."}

BRANCO = "\033[1;36m"
VERMELHO = "\033[31m"
VERDE = "\033[1;32m"
AZUL = "\033[1;34m"
AMARELO = "\033[1;33m"
CIANO = "\033[1;36m"
RESET = "\033[0m"

class Locacao:
    def __init__(self, placa_carro, cpf_cliente, data_retirada, data_entrega):
        self.placa_carro = placa_carro
        self.cpf_cliente = cpf_cliente
        self.data_retirada = data_retirada
        self.data_entrega = data_entrega
        self.valor_servico = (self.data_entrega - self.data_retirada).days * 120

    def mostrar_informacoes(self):
        print(f"PLACA: {self.placa_carro} CPF: {self.cpf_cliente}")
        print(f"DATA DE RETIRADA: {self.data_retirada.strftime('%d/%m/%Y')} DATA DE ENTREGA: {self.data_entrega.strftime('%d/%m/%Y')}")
        print(f"VALOR DO SERVIÇO: R${self.valor_servico:.2f}")

def criar_menu(lista: list)  -> None:
    """
    Criar menu de opções.

    Args:
        lista (list): Lista de opções que devem ser adicionadas ao menu.
    """
    
    for i,item in enumerate(lista,start=1):
        print(f"{i} - {CIANO}{item}{RESET}")
    criar_linha("-")

def criar_linha(caracter: str, tamanho = 50) -> None:
    """
    Cria uma linha com o caracter escolhido.

    Args:
        caracter (str): Caracter que será usado para criar a linha.
        tamanho (int, optional): Quantidade de caracteres que irá formar a linha. 
                                 Como default o valor é 50.

    Returns:
        None
    """
    print(caracter * tamanho)

def criar_cabecalho(mensagem: str, tamanho: int, cor: str) -> None:
    """
    Criar um cabeçalho estruturado e centralizado.

    Args:
        mensagem (str): Mensagem que deverá ser apresentada no cabeçalho.
        tamanho (int): Tamanho que terá o cabeçalho.
        cor (str): Informação da cor que será utilizada.
    """
    criar_linha("-")
    print(f"{cor}{mensagem.center(tamanho)}{RESET}")
    criar_linha("-")

def pausar() -> None:
    """
    Cria uma pausa no sistema até que seja presionada qualquer tecla.
    """
    input("\nPressione uma tecla para continuar...\n")

def verificar_lista(lista_locacoes: list) -> bool:
    """
    Verifica se uma lista contêm dados gravados.

    Args:
        lista_locacoes (list): Lista que será verificada.

    Returns:
        bool: Retorna True se a lista contêr dados ou False se a lista estiver vazia.
    """
    return not lista_locacoes

def verificar_numero(mensagem: str) -> int:
    """
    Verifica se a informação que está sendo digitada é um número inteiro

    Args:
        mensagem (str): Texto que será exibido para o usuário.

    Returns:
        int: Retorna o número válido.
    """
    while True:
        try:
            numero = int(input(f"{AZUL}{mensagem}{RESET}"))
        except (ValueError, TypeError):
            mostrar_erro("E01", VERMELHO)
        else:
            return numero
        
def verificar_data(mensagem: str) -> datetime:
    """
    Efetua tratamento de erro na digitação de data.

    Args:
        mensagem (str): Texto que será apresentado para usuário.

    Returns:
        datetime: Data validada pelo sistema.
    """
    while True:
        try:
            data = datetime.strptime(input(mensagem), "%d/%m/%Y")
        except (ValueError, TypeError):
            mostrar_erro("E03", VERMELHO)
        else:
            return data

def mostrar_erro(codigo: str, cor: str) -> None:
    """
    Mostra a mensagem de erro com a cor de texto escolhida.

    Args:
        codigo (str): Código do erro
        cor (str): Cor escolhida
    """
    print(f"\n{cor}=== {MENSAGEM_ERRO.get(codigo)} ==={RESET}")

def cadastrar_locacoes(lista_locacoes: list):
    criar_cabecalho("CADASTRO DE LOCAÇÕES", 50, VERDE)
    
    placa = input("PLACA: ")
    cpf = input("CPF: ")
    retirada = verificar_data("DATA DE RETIRADA (DD/MM/AAAA): ")
    
    while True:
        entrega = verificar_data("DATA ENTREGA (DD/MM/YYYY): ")
        if entrega >= retirada:
            break
        else:
            mostrar_erro("E02", VERMELHO)

    dados_locacao = Locacao(placa_carro=placa, cpf_cliente=cpf, data_retirada=retirada, 
                            data_entrega=entrega)
    lista_locacoes.append(dados_locacao)

    criar_cabecalho("LOCAÇÃO CADASTRADA COM SUCESSO!", 50, "\033[32m")
    pausar()

def listar_locacoes(lista_locacoes: list):
    criar_cabecalho("LISTAGEM DE LOAÇÕES", 50, "\033[32m")

    if verificar_lista(lista_locacoes):
        mostrar_erro("E04", AMARELO)
        pausar()
        return
    
    for dado in lista_locacoes:
        dado.mostrar_informacoes()
        criar_linha("-")

    pausar()

def buscar_locacoes_placa(lista_locacoes: list):
    encontrou = False

    criar_cabecalho("BUSCAR LOCAÇÕES POR PLACA", 50, "\033[32m")

    if verificar_lista(lista_locacoes):
        mostrar_erro("E04", AMARELO)
        pausar()
        return
    
    placa = input("Digite a placa: ")

    for dados in lista_locacoes:
        if placa == dados.placa_carro:
            dados.mostrar_informacoes()
            encontrou = True
            pausar()
    if not encontrou:
        mostrar_erro("E05", AMARELO)

def buscar_locacoes_cpf(lista_locacoes: list):
    encontrou = False

    criar_cabecalho("BUSCAR LOCAÇÕES POR CPF", 50, "\033[32m")

    if verificar_lista(lista_locacoes):
        mostrar_erro("E04", AMARELO)
        pausar()
        return

    cpf = input("Digite CPF: ")

    for dados in lista_locacoes:
        if cpf == dados.cpf_cliente:
            dados.mostrar_informacoes()
            encontrou = True
            pausar()

    if not encontrou:
        mostrar_erro("E06", AMARELO)

def fechar_programa(lista_locacoes: list):
    print("\nSistema encerrado.\n")
    exit()

def main():
    lista_locacoes = []

    acoes = {1: cadastrar_locacoes,
         2: listar_locacoes,
         3: buscar_locacoes_placa,
         4: buscar_locacoes_cpf,
         5: fechar_programa}
    
    while True:
        criar_cabecalho("SISTEMA DE LOCAÇÃO DE VEÍCULOS", 50, "\033[32m")
        criar_menu(["CADASTRO DE LOCAÇÃO", "LISTAGEM DE LOCAÇÕES", "BUSCA DE LOCAÇÃO POR PLACA DO VEÍCULO", ""
                    "BUSCA DE LOCAÇÃO POR CPF DO CLIENTE", "FECHAR PROGRAMA"])

        escolha = verificar_numero("Digite a opção desejada: ")

        funcao_escolhida = acoes.get(escolha)

        if funcao_escolhida:
            funcao_escolhida(lista_locacoes)
        else:
            mostrar_erro("E07", VERMELHO)
            pausar()

if __name__ == "__main__":
    main()