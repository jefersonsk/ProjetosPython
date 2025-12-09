telefones = set()
quantidade = int(input())
contador = 0
validar = True

for x in range(0, quantidade):
    telefones.add(input())

print(telefones[0].difference(telefones[1]))