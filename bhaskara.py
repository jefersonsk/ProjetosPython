def calcula_bhaskara(a: int, b: int, c: int) -> float:
    delta = b**2 - (4*a*c)
    print(delta)
    x1 = (- b + (delta * 0.5)) / 2 * a
    x2 = (- b - (delta * 0.5)) / 2 * a
    
    return x1, x2

a, b, c = input().split(" ")
resultado = calcula_bhaskara(int(a), int(b), int(c))
print(resultado)