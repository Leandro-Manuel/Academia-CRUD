#conectou a biblioteca no banco de dados

from teste import *
cursor = banco.cursor()

#inserir = f"INSERT INTO alunos (atributo) values ('{nome}','{cpf}','{endereco}');"
#cursor.execute(inserir)


def inserir_alunos(nome,cpf,endereco,telefone,email):
    inserir = f"INSERT INTO alunos (nome,cpf,endereco,telefone,email) VALUES ('{nome}','{cpf}','{endereco}','{telefone}','{email}');"
    cursor.execute(inserir)
    banco.commit()

def deletar_alunos(delete):
    deletar = 'DELETE FROM aluno WHERE id_aluno = %s'
    data = (delete)
    cursor.execute(deletar,data)
    banco.commit()

def inserir_modalidades(nome):
    inserir = f"INSERT INTO modalidades (nome) VALUES ('{nome}');"
    cursor.execute(inserir)
    banco.commit()

def inserir_func(nome,cpf,departamento,salario,qtdfilhos):
    inserir = f"INSERT INTO func (nome,cpf,departamento,salario,qtdFilhos) VALUES ('{nome}','{cpf}','{departamento}','{salario}','{qtdfilhos}');"
    cursor.execute(inserir)
    banco.commit()

def inserir_personal(cpf,cref,nome,telefone,endereco,email):
    inserir = f"INSERT INTO personal (cpf,cref,nome,telefone,endereco,email) VALUES ('{cpf}','{cref}','{nome}','{telefone}','{endereco}','{email}');"
    cursor.execute(inserir)
    banco.commit()

