contador = 0 # Variável Global

def incrementar_global():
    # Declara que estamos usando a variável global 'contador'
    global contador 
    contador += 1
    print(f"Dentro da função: {contador}")

print(f"Antes da chamada: {contador}")
incrementar_global()
incrementar_global()
print(f"Depois da chamada: {contador}")
# Saída:
# Antes da chamada: 0
# Dentro da função: 1
# Dentro da função: 2
# Depois da chamada: 2