a, b, c = map(float, input().split(" "))

delta = b**2 - 4 * a * c

if a <= 0 or delta < 0:
    print("Impossivel calcular")
else:
    x_um = (-b + delta ** 0.5) / (2 * a)
    x_dois = (-b - delta ** 0.5) / (2 * a)
    print(f"R1 = {x_um:.5f}")
    print(f"R2 = {x_dois:.5f}")
