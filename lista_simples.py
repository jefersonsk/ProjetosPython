lista_multiplicada = []

lista = input().split(" ")

for x in range(0, 8):
    multiplica_lista = int(lista[x])
    multiplica_lista = multiplica_lista * 2
    lista_multiplicada.append(multiplica_lista)
    multiplica_lista = 0
    
print(f'A: ', *lista)
print(f'B: ', *lista_multiplicada)