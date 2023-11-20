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

nmr_menu_principal = 0
nmr_menu_secundaria = 0

while True:
    print('=='*9 + 'MENU' + '=='*12)
    escolha1 = int(input('Digite 1 para selecionar a tabela alunos.\n'
                         'Digite 2 para selecionar a tabela modalidades.\n'
                         'Digite 3 para selecionar a tabela funcionarios.\n'
                         'Digite 4 para selecionar a personal.\n'
                         'Digite 5 para sair do programa.\n'
                         + '==' * 23 + '\n'
                         'Resposta: '))
    if escolha1 == 1:
        nmr_menu_principal = 1

    elif escolha1 == 2:
        nmr_menu_principal = 2

    elif escolha1 == 3:
        nmr_menu_principal = 3

    elif escolha1 == 4:
        nmr_menu_principal = 4

    else:
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
        if escolha2 == 1:
            nmr_menu_secundaria = 1

        elif escolha2 == 2:
            nmr_menu_secundaria = 2

        elif escolha2 == 3:
            nmr_menu_secundaria = 3

        elif escolha2 == 4:
            nmr_menu_secundaria = 4

        else:
            break

        if nmr_menu_principal == 1 and nmr_menu_secundaria == 1:
            nome = input('Digite o seu nome: ')
            cpf = input('Digite o seu cpf: ')
            endereco = input('Digite o seu endereço: ')
            telefone = input('Digite o número do seu telefone: ')
            email = input('Digite o seu e-mail: ')
            inserir_alunos(nome,cpf,endereco,telefone,email)

        if nmr_menu_principal == 2 and nmr_menu_secundaria == 1:
            nome = input('Digite o nome da modalidade: ')
            inserir_modalidades(nome)

        if nmr_menu_principal == 3 and nmr_menu_secundaria == 1:
            nome = input('Digite o nome do funcionário: ')
            cpf = input('Digite o cpf: ')
            departamento = input('Digite o número do departamento: ')
            salario = input('Digite o salário do funcionário: ')
            qtdFilhos = input('Informe a quantidade de filho do funcionário: ')
            inserir_func(nome,cpf,departamento,salario,qtdFilhos)

        if nmr_menu_principal == 4 and nmr_menu_secundaria == 1:
            cpf = input('Digite o número de cpf: ')
            cref = input('Digite o número do cref: ')
            nome = input('Digite o nome do personal: ')
            telefone = input('Digite o número de telefone: ')
            endereco = input('Digite o endereço: ')
            email = input('Digite o email: ')
            inserir_personal(cpf,cref,nome,telefone,endereco,email)

        







