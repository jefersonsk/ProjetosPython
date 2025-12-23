palavras = ("Jeferson", "Edna", "Felipe")

for x in palavras:

    print(f"\nNa palavra {x.upper()} temos: ", end=" ")

    for letra in x:
        if letra.lower() in "aeiou":
            print(f"{letra.lower()}", end=" ")