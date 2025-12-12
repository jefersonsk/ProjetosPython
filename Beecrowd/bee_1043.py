a, b, c = map(float, input().split(" "))

if a + b > c  and b + c > a and a + c > b:
    resultado = a + b + c
    print(f"Perimetro = {resultado:.1f}")
else:
    resultado = ((a + b) * c) / 2
    print(f"Area = {resultado:.1f}")