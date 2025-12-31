def calcula_metades(valor_inicial: float, divisor: int, repeticao: int) -> list:
    """Calcula uma sequência dividindo o número anterior por um divisor.

    Args:
        valor_inicial (float): O primeiro valor da sequência.
        divisor (int): O valor pelo qual os números serão divididos.
        repeticao (int): A quantidade total de itens na lista gerada.

    Returns:
        list: Uma lista contendo a sequência calculada.
    """
    numeros = [valor_inicial]
    # O _ é utilizado por convenção quando a variável do for não utilizadas para cálculos
    for _ in range(1, repeticao):
        # O -1 pega o último valor de uma lista
        numeros.append(numeros[-1] / divisor)

    return numeros

def executar_testes():
    print("Rodando autoteste...")

    resultado = calcula_metades(100.0, 2, 3)
    assert resultado == [100.0, 50.0, 25.0]
    
    print("Autoteste Passou!")

REPETICAO = 100
flag = True

while flag:
    try:
        numero = float(input())
    except ValueError:
        print("ERRO: Digite um valor válido para o cálculo")
    else:
        flag = False

lista = calcula_metades(numero, 2, REPETICAO)

for posicao, numero in enumerate(lista):
    print(f"N[{posicao}] = {numero:.4f}")