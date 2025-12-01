# 1. Leitura dos dados
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

# 2. Verificação da ordem (O "truque" da inversão)
invertido = False
if inicio > fim:
    inicio, fim = fim, inicio  # Troca os valores
    invertido = True           # Marca a bandeira

# 3. Variável de passo (o "i" que controla a linha)
i = 0

# 4. Laço Principal
# Enquanto o "lado esquerdo" (inicio + i) for menor ou igual ao "lado direito" (fim - i)
while (inicio + i) <= (fim - i):
    
    # Bloco Início: cresce da esquerda
    # Vai de 'inicio' até 'inicio + i'
    parte_1 = list(range(inicio, inicio + i + 1))
    
    # Bloco Fim: cresce da direita
    # AQUI está a mágica do MAX que conversamos:
    # O início deste bloco é o maior entre:
    #   a) Onde ele "deveria" começar (fim - i)
    #   b) O número logo após o fim da parte_1 (inicio + i + 1)
    comeco_parte_2 = max(fim - i, inicio + i + 1)
    
    parte_2 = list(range(comeco_parte_2, fim + 1))
    
    # Junta as duas partes
    resultado = parte_1 + parte_2
    
    # 5. Verifica se precisa inverter antes de imprimir
    if invertido:
        print(*resultado[::-1]) # Imprime invertido se a entrada original era decrescente
    else:
        print(*resultado)       # Imprime normal
        
    # Passa para a próxima linha
    i += 1