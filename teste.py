import mysql.connector
banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '302302',
    database = 'academiaturmad'
)

print(banco)
meucursor = banco.cursor()

from biblioteca import *

while True:
    print('=='*9 + 'MENU' + '=='*12)
    escolha1 = int(input('Digite 1 para selecionar a tabela alunos.\n'
                         'Digite 2 para selecionar a tabela modalidades.\n'
                         'Digite 3 para selecionar a tabela funcionarios.\n'
                         'Digite 4 para selecionar a personal.\n'
                         'Digite 5 para sair do programa.\n'
                         + '==' * 23 + '\n'
                         'Resposta: '))
        if escolha1 == 5:
            break

    while True:
        print('==' * 23)
        escolha2 = int(input('Digite 1 para Inserir.\n'
                             'Digite 2 para deletar.\n'
                             'Digite 3 para alterar.\n'
                             'Digite 4 para ler.\n'
                             'Digite 5 para voltar.\n'
                             + '==' * 23 + '\n'
                             'Resposta: '))
            if escolha2 == 5:
                break

        if escolha1 == 1:
            if escolha2 == 1:
                nome = input('Digite o seu nome: ')
                cpf = input('Digite o seu cpf: ')
                endereco = input('Digite o seu endereço: ')
                telefone = input('Digite o número do seu telefone: ')
                email = input('Digite o seu e-mail: ')
                inserir_alunos(nome, cpf, endereco, telefone, email)

            elif escolha2 == 2:

            elif escolha2 == 3:

            else:


        if escolha1 == 2 and escolha2 == 1:
            nome = input('Digite o nome da modalidade: ')
            inserir_modalidades(nome)

        if escolha1 == 3 and escolha2 == 1:
            nome = input('Digite o nome do funcionário: ')
            cpf = input('Digite o cpf: ')
            departamento = input('Digite o número do departamento: ')
            salario = input('Digite o salário do funcionário: ')
            qtdFilhos = input('Informe a quantidade de filho do funcionário: ')
            inserir_func(nome,cpf,departamento,salario,qtdFilhos)

        if escolha1 == 4 and escolha2 == 1:
            cpf = input('Digite o número de cpf: ')
            cref = input('Digite o número do cref: ')
            nome = input('Digite o nome do personal: ')
            telefone = input('Digite o número de telefone: ')
            endereco = input('Digite o endereço: ')
            email = input('Digite o email: ')
            inserir_personal(cpf,cref,nome,telefone,endereco,email)









