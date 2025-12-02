def media_alunos(nota_01: float, nota_02: float, nota_03: float, tipo_media: str) -> float:
    if tipo_media.upper() == "A":
        resultado = (nota_01 + nota_02 + nota_03) / 3
    elif tipo_media.upper() == "P":
        resultado = ((nota_01 * 5) + (nota_02 * 3) + (nota_03 * 2)) / 10
    elif tipo_media.upper() == "H":
        resultado = 3 / ((1/nota_01) + (1/nota_02) + (1/nota_03))

    return resultado

nota_01, nota_02, nota_03, tipo_media = input("Digite as notas e tipo de média a ser calculada (M)édia Artitmética, Média (P)onderada ou Média (H)armônica: ").split(" ")
if tipo_media.upper() == "A" or tipo_media.upper() == "P" or tipo_media.upper() == "H":
    resultado = media_alunos(float(nota_01), float(nota_02), float(nota_03), tipo_media)
    print(f"A média é: {resultado:.1f}, para a opção {tipo_media.upper()}")
else:
    print("Opção inválida")