flag = True
flag_tempo = True

while flag:

    try:
        if flag_tempo:
            tempo = int(input("Tempo: "))
            if tempo > 0:
                flag_tempo = False
            else:
                raise TypeError("Erro 1")

        velocidade = float(input("Velocidade: "))
        if velocidade <= 0:
            raise TypeError("Erro 1")
        flag = False

    except ValueError:
        print("Você não pode digitar letras!")
    except TypeError:
        print("Valor deve ser positivo")

print(f"Quantidade: {(tempo * velocidade) / 12:.3f}")