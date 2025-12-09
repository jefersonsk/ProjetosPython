flag = True

while flag:
    try:
        numero = int(input("Digite um número: "))

        if numero <= 0:
            raise TypeError("Customizado 1")
        else:
            for n in range(1, numero + 1):
                print(n,end=' ')
            flag = False

    except ValueError:
        flag = False
        print("Somente números devem ser digitados.")
    except TypeError:
        print("Somente deve ser digitado número maior que 0.")


