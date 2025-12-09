GASOLINA = 4.97
ALCOOL = 5.78
valor = 0.0

# flags para validação de combustível e litros

valido_combustivel = valido_litros = False

nome = input("Digite o seu nome: ")

print(f"Olá {nome}!!!")

combustivel = input("Digite G - Gasolina e A - Alcool: ")
litros = float(input("Digite a quantidade de litros: "))

letra = combustivel.upper().strip()[0]

if letra == "G":
    valor = GASOLINA * litros
    valido_combustivel = True
if letra == "A":
    valor = ALCOOL * litros
    valido_combustivel = True

if litros > 0:
    valido_litros = True
    
if valido_litros and valido_combustivel:
    print(f'Valor total: R$ {valor:.2f}')
else:
    print("Dados inválido!")