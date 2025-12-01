# VARIÁVEIS
jogadores = []
sba_dado = []
sba_efetivo = []
total_saque_dado = 0
total_bloqueio_dado = 0
total_ataque_dado = 0
total_saque_efetivo = 0
total_bloqueio_efetivo = 0
total_ataque_efetivo = 0

# ENTRADA DE DADOS
numero = int(input())

for x in range(0, numero):

    jogadores.append(input())
    sba_dado.append(input().split(" "))
    sba_efetivo.append(input().split(" "))

# PROCESSAMENTO
for x in range(0, numero):
    total_saque_dado = total_saque_dado + int(sba_dado[x][0])
    total_bloqueio_dado = total_bloqueio_dado + int(sba_dado[x][1])
    total_ataque_dado = total_ataque_dado + int(sba_dado[x][2])
    total_saque_efetivo = total_saque_efetivo + int(sba_efetivo[x][0])
    total_bloqueio_efetivo = total_bloqueio_efetivo + int(sba_efetivo[x][1])
    total_ataque_efetivo = total_ataque_efetivo + int(sba_efetivo[x][2])

pontos_saque = (total_saque_efetivo * 100) / total_saque_dado
pontos_bloqueio = (total_bloqueio_efetivo * 100) / total_bloqueio_dado
pontos_ataque = (total_ataque_efetivo * 100) / total_ataque_dado

# SAÍDA DE DADOS
print(f"Pontos de Saque: {pontos_saque:.2f}%")
print(f"Pontos de Bloqueio: {pontos_bloqueio:.2f}%")
print(f"Pontos de Ataque: {pontos_ataque:.2f}%")