a, b, c, d = map(int, input().split(" ")) # converte vários dados para o tipo solicitado

status = "Valores aceitos" if (b > c) and (d > a) and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0 else "Valores nao aceitos"

print(status)