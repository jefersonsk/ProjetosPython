subfilo, classe, dieta = input().lower().split(" ")

if subfilo == "vertebrado":
    if classe == "ave":
        if dieta == "carnivoro":
            especie = "aguia"
        else:
            especie = "pomba"
    else:
        if dieta == "onivoro":
            especie = "homem"
        else:
            especie = "vaca"
else:
    if classe == "inseto":
        if dieta == "hematofago":
            especie = "pulga"
        else:
            especie = "lagarta"
    else:
        if dieta == "hematofago":
            especie = "sanguessuga"
        else:
            especie = "minhoca"

print(especie)