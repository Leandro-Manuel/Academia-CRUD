import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '302302',
    database = 'academiaturmad'
)

print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos'; #poderia colocar outra entidade
meucursor.execute(pesquisa)
#fetchall recebe tudo da pesquisa
#e retorna atraves de uma tupla
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

nome = 'Leandrou'
telefone = '11111111111'
sql = 'INSERT INTO alunos (nome,telefone) VALUES(%s,%s)'
data = (nome,telefone)
meucursor.execute(sql,data)
banco.commit()
meucursor.close()
banco.close()