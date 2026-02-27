# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a 
# variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. 
# Apresentar os valores trocados.

a, b = input("Digite 2 números separados por espaço: ").split(" ")

a, b = b, a # Atribução múltipla(Tuple unpacking)

print(f"Posição dos números digitados trocados: {a} {b}")