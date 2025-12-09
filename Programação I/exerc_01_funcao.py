def calcula_volume(raio: float) -> str:
    PI = 3.14
    v = (4 * PI * raio**3) / 3
    return v

raio = float(input("Digite o raio: "))
print(calcula_volume(raio))
