tipos_triangulos = []

lados = sorted(list(map(float, input().split(" "))), reverse=True)

a, b, c = lados

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else: 
    if a **2 == b ** 2 + c ** 2:
        tipos_triangulos.append("TRIANGULO RETANGULO")
    if a ** 2 > b ** 2 + c ** 2:
        tipos_triangulos.append("TRIANGULO OBTUSANGULO")
    if a ** 2 < b ** 2 + c ** 2:
        tipos_triangulos.append("TRIANGULO ACUTANGULO")
    if a == b and a == c and b == c:
        tipos_triangulos.append("TRIANGULO EQUILATERO")
    elif a== b or a == c or b == c:
        tipos_triangulos.append("TRIANGULO ISOSCELES")

    for x in tipos_triangulos:
        print(x)