from funcoes import verifica_primo

# ENTRADA DE DADOS
conta_primo = 1
loop =  2

numero = int(input())

# PROCESSAMENTO / CÁLCULOS / SAÍDA DE DADOS
while loop < numero:
    
    for x in range(2, loop + 1):
        
        if loop % x == 0:
            conta_primo += 1
    
    if conta_primo == 2:
        print(loop)
    
    conta_primo = 1
    loop += 1