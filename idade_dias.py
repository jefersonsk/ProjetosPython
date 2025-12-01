flag = True

while flag:

    try:
        dias = int(input())
        if dias <= 0:
            raise ValueError("Erro 1")
        else:
            flag = False
    
    except:
        print("Digite um valor positivo")

anos = dias // 365
meses = (dias - (anos * 365)) // 30
dias = (dias - (anos * 365) - (meses * 30))

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')