# ENTRADA DE DADOS
x1, y1 = input().split(" ")
x2, y2 = input().split(" ")

# CASTING
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

# PROCESSAMENTO
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# SAÍDA DE DADOS
print(f"{distancia:.4f}")