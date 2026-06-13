import mysql.connector

# Estabelece a conexão com o banco
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='floricultura'
)

# Criando uma variável para executar a sentença SQL
mycursor = mydb.cursor()

cre = input("CRE:")
nome = input("NOME:")
email = input("EMAIL: ")
data_nascimento = input("DATA NASCIMENTO: ")
sexo = input("SEXO: ")

val = (cre, nome, email, data_nascimento, sexo)

# Os $ são validação de dados
mycursor.execute(
    "INSERT INTO enfermeiras (numero_cre, nome, endereco_email, data_nascimento, sexo) VALUES ($s, $s, $s, $s, $s)", val)

# Comando para salvar dados no Banco de Dados
mydb.commit()

sql = "INSERT INTO enfermeiras (numero_cre, nome, endereco_email, data_nascimento, sexo) VALUES ('123', 'Maria', '123@gmail', '1998-05-04', 'FEMININO')"

# Encerra a conexão do banco
mydb.close()

myresult = mydb.fetc
