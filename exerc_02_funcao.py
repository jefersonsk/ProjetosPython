def calcula_media(nota_01: float, nota_02: float, nota_03: float, opcao: str) -> str:
    if opcao.upper() == "A":
        media = (nota_01 + nota_02 + nota_03) / 3
    elif opcao.upper() == "P":
        media = ((nota_01 * 5) + (nota_02 * 3) + (nota_03 * 2)) / 10
    elif opcao.upper() == "H":
        media = 3 / (1/nota_01 + 1/nota_02 + 1/nota_03)

    return media

a = float(input("Nota 01: "))
b = float(input("Nota 02: "))
c = float(input("Nota 03: "))
o = input("Opção: ")
print(f"{calcula_media(a, b, c, o):.2f}")