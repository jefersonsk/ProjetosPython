import os
import csv

from datetime import datetime

def validar() -> str:

    flag = True

    while flag:
        validar = input("Deseja continuar S/N? ").upper()
        if validar != "S" and validar != "N":
            print("Digite uma opção válida.")
        else:
            flag = False
    
    return validar

def converter_data(texto_para_data: str) -> datetime:

    return datetime.strptime(texto_para_data, "%d/%m/%Y")

def linha_cabecalho(tam = 60):
    return '-' * tam

def cabecalho(texto: str) -> str:
    print(linha_cabecalho())
    print(texto.center(60))
    print(linha_cabecalho())

def valida_numero(pergunta: str, tipo: int | float | datetime, mensagem_erro: str) -> int | float | datetime:
    flag = True
    while flag:
        try:
            validar = tipo(input(pergunta))
            flag = False
        except ValueError:
            print(mensagem_erro)

    return validar

def valida_vazio(pergunta: str) -> str:
    flag = True
    while flag:
        validar = input(pergunta)
        if validar.strip() == "":
            print("ERRO: Campo não pode ser vazio.")
        else:
            flag = False
            return validar

# VARIÁVEIS

nome = "NOME"
idade = "IDADE"
profissao = "PROFISSÃO"
data_consulta = "DATA DA CONSULTA"
motivo = "MOTIVO DA CONSULTA"
data_retorno = "DATA DE RETORNO"
valor_consulta = "VALOR DA CONSULTA"
registro = [nome, idade, profissao, data_consulta, motivo, data_retorno, valor_consulta]
contador = 0
valor_total = 0
repetir = "S"
totais_por_dia = {}
flag = True

# Retorna booleano caso o arquivo exista ou não.
arquivo_existe = os.path.exists('consultas.csv')

cabecalho("SISTEMA DE CONSULTAS")

with open("consultas.csv", "a") as arquivo:
    # Se o arquivo não existe(False), cria o cabeçalho do arquivo
    if arquivo_existe == False:
        linha = ','.join(registro)
        arquivo.write(linha + "\n")

    while repetir != "N":
        
        nome = valida_vazio("Nome: ")
        idade = valida_numero("Idade: ", int, "ERRO: Digite apenas números.")
        profissao = input("Profissão: ")
        data_consulta = datetime.now()
        motivo = valida_vazio("Motivo da consulta: ")
        data_retorno = valida_numero("Data de retorno: ", converter_data, "ERRO: Digite uma data válida.")
        valor_consulta = valida_numero("Valor da consulta: R$ ", float, "ERRO: Digite um valor válido.")
        registro = [nome, str(idade), profissao, data_consulta.strftime("%d/%m/%Y"), motivo, data_retorno.strftime("%d/%m/%Y"), str(valor_consulta)]
        linha = ','.join(registro)
        arquivo.write(linha + "\n")
        print("Registro concluído.")
        repetir = validar()
        
arquivo.close()

# Criação de dicionário com as informações de data, número de consultas nessa data e o valor total de consultas nesse dia
with open("consultas.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        aux_data = dados[3]
        aux_valor = float(dados[6])
        if aux_data in totais_por_dia:
            contador = totais_por_dia[aux_data][0]
            contador = contador + 1
            valor_atual = totais_por_dia[aux_data][1]
            valor_atual = valor_atual+ aux_valor
            totais_por_dia[aux_data] = [contador, valor_atual]
        else:
            totais_por_dia.update({aux_data: [1, aux_valor]})

arquivo.close()

# SAÍDA DE DADOS

# Ordena as datas que estão no dicionário e coloca em uma lista.
datas_ordenadas = sorted(totais_por_dia, key=converter_data)

cabecalho("RELATÓRIO DIÁRIO")

for dados in datas_ordenadas:
    lista_valores = totais_por_dia.get(dados)
    print(f"{dados}: {lista_valores[0]} consultas - Total: R$ {lista_valores[1]:.2f}")

cabecalho("SAINDO DO SISTEMA")