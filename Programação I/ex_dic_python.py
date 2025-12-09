di = {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Claudia': 'Java', 'Mauro': 'PHP'}
x = di.items()
print(x)
for k, v in x:
    print('chave:', k, end = ", ")
    print('valor:', v)