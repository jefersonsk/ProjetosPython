arquivo = open("novo_arquivo.txt", 'w')

arquivo.write("Eu amo programar!\n")
arquivo.write("\n\n\n")
arquivo.write("\tcontando... \n\n")

for x in range(1000):
    arquivo.write(f"nr - {x}\n")

arquivo.close()