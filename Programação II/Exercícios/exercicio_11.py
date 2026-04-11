# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, 
# nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

numero_eleitores = int(input("Digite número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos em branco: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

print(f"Percentual de votos brancos: {(votos_brancos * 100) / numero_eleitores}")
print(f"Percentual de votos nulos: {(votos_nulos * 100) / numero_eleitores}")
print(f"Percentual de votos válidos: {(votos_validos * 100) / numero_eleitores}")