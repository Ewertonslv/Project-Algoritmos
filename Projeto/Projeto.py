import re
import pickle
alunosword = {}
alunospowerpoint = {}
alunosexcel = {}
cpfsword = []
cpfspowerpoint = []
cpfsexcel = []
notasword = {}
notaspowerpoint = {}
notasexcel = {}



def salvar():
    arq = open('alunosword.txt','wb')
    pickle.dump(alunosword, arq)
    arq.close()
    arq1 = open('alunospowerpoint.txt','wb')
    pickle.dump(alunospowerpoint, arq1)
    arq1.close()
    arq2 = open('alunosexcel.txt','wb')
    pickle.dump(alunosexcel, arq2)
    arq2.close()

def ler():
    arq = open('alunosword.txt','rb')
    alunosword = pickle.load(arq)


    arq1 = open('alunospowerpoint.txt','rb')
    alunospowerpoint = pickle.load(arq1)


    arq2 = open('alunosexcel.txt','rb')
    alunosexcel = pickle.load(arq2)




def turma():

    print('-' * 40)
    print('''1 - Turma de WORD
2 - Turma de POWER POINT
3 - Turma de EXCEL''')
    print('-' * 40)

def menu_inicial():
    print('''1 - Matricular Aluno
2 - Turmas
3 - Buscar
4 - Sair''')

def barra (): #Formatação
    print('=' * 40)

def validar_nome():  # validar nome
    global nome
    aux = 1
    nome = input('Digite o nome do aluno: ')
    while aux == 1:

        if re.match("[^0-9][A-Za-z-ãõçóéúáí ]{3,}", nome):
            aux = 0
        else:
            print('Voçe digitou um caractere invalido!')
            nome = input('Digite o nome do aluno: ')

def validar_cpf(cpf):

    cpflista = list(cpf)
    pesos1 = [p1 for p1 in range(10, 1, -1)]
    pesos2 = [p2 for p2 in range(11, 1, -1)]
    somapeso1, somapeso2 = 0, 0


    for i in range(9):
        somapeso1 += pesos1[i] * int(cpflista[i])

    for i in range(10):
        somapeso2 += pesos2[i] * int(cpflista[i])

    resto1 = somapeso1 % 11
    resto2 = somapeso2 % 11

    if 11 - resto1 > 9:
        verificador1 = '0'
    else:
        verificador1 = str(11 - resto1)

    if 11 - resto2 > 9:
        verificador2 = '0'
    else:
        verificador2 = str(11 - resto2)

    if verificador1 == cpflista[9] and verificador2 == cpflista[10]:
        return cpf

def validar_celular():
    cont = True
    global celular
    while cont == True:
        try:
            if len(celular) != 11:
                raise ValueError
            else:
                celular = int(celular)  # se contiver letras causa um ValueError
                celular = str(celular)
                numeroCelular = celular

                cont = False

        except ValueError:
            if len(celular) == 0:
                print('Você não digitou o número')
                celular = input('Digite um número para contato: ')
            else:
                print('Número inválido, o número precisa ter 11 números inteiros')
                celular = input('Digite um número para contato: ')

def validar_email():
    global email
    validar = 1
    while validar == 1:
        if len(email) <= 5:
            email = input('Digite o E-mail do aluno: ')
        else:
            if not '@' in email:
                email = input('Digite o E-mail do aluno: ')
            else:
                if not email.endswith('.com'):
                    email = input('Digite o E-mail do aluno: ')
                else:
                    validar = 0

def validar_segundo_celular():
    cont = True
    global telefone
    while cont == True:
        try:
            if len(telefone) != 11:
                raise ValueError
            else:
                telefone = int(telefone)  # se contiver letras causa um ValueError
                telefone = str(telefone)
                numeroCelular = telefone

                cont = False

        except ValueError:
            if len(telefone) == 0:
                print('Você não digitou o número')
                telefone = input('Digite um segundo número para contato: ')
            else:
                print('Número inválido, o número precisa ter 11 números inteiros')
                telefone = input('Digite um segundo número para contato: ')

def matricular_aluno_word(): # Função para metricular o aluno
    print()
    print("MATRICULA TURMA DE WORD: ")
    print()
    global cpf
    cpf = input('Digite o número de CPF: ')
    entra = True
    while entra == True:
        if cpf == '00000000000':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '11111111111':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '22222222222':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '33333333333':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '44444444444':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '55555555555':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '66666666666':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '77777777777':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '88888888888':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '99999999999':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        try:
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            if re.search(r"^\d{11}$", cpf):
                if validar_cpf(cpf) == cpf:
                    entra = False
                else:
                    print("\nO numero {} é um numero de CPF invalido.\n".format(
                        cpf)
                    )
                    cpf = input('Digite o número de CPF: ')
            else:
                raise ValueError

        except ValueError:
            if cpf == '':
                print("Voce não informou o CPF!")
                cpf = input('Digite o número de CPF: ')

            elif re.search(r"^(\D+|\..*-_?)$", cpf):
                print("Informe apenas números!")
                cpf = input('Digite o número de CPF: ')
            else:
                print("Informe os 11 digitos do CPF!")
                cpf = input('Digite o número de CPF: ')

    validar_nome()
    global telefone
    telefone = input('Digite um número para contato: ')
    validar_segundo_celular()
    global celular
    celular = input('Digite um segundo número para contato: ' )
    validar_celular()
    global email
    email = input('Digite o E-mail do aluno: ')
    validar_email()
    alunosword[cpf] = [nome, telefone, celular, email]
    cpfsword.append(cpf)

    print("Matricula realizada com sucesso!")

def matricular_aluno_powerpoint(): # Função para metricular o aluno
    print('')
    print("MATRICULA TURMA DE POWERPOINT: ")
    print('')
    global cpf
    entra = True
    cpf = input('Digite o número de CPF: ')
    while entra == True:
        if cpf == '00000000000':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '11111111111':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '22222222222':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '33333333333':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '44444444444':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '55555555555':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '66666666666':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '77777777777':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '88888888888':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '99999999999':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        try:
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            if re.search(r"^\d{11}$", cpf):
                if validar_cpf(cpf) == cpf:


                    entra = False
                else:
                    print("\nO numero {} é um numero de CPF invalido.\n".format(
                        cpf)
                    )
                    cpf = input('Digite o número de CPF: ')
            else:
                raise ValueError

        except ValueError:
            if cpf == '':
                print("Voce não informou o CPF!")
                cpf = input('Digite o número de CPF: ')

            elif re.search(r"^(\D+|\..*-_?)$", cpf):
                print("Informe apenas números!")
                cpf = input('Digite o número de CPF: ')
            else:
                print("Informe os 11 digitos do CPF!")
                cpf = input('Digite o número de CPF: ')
    validar_nome()
    global telefone
    telefone = input('Digite um número para contato: ')
    validar_segundo_celular()
    global celular
    celular = input('Digite um segundo número para contato: ')
    validar_celular()
    global email
    email = input('Digite o E-mail do aluno: ')
    validar_email()
    alunospowerpoint[cpf] = [nome, telefone, celular, email]
    cpfspowerpoint.append(cpf)

    print("Matricula realizada com sucesso!")

def matricular_aluno_excel():  # Função para metricular o aluno
    print('')
    print("MATRICULA TURMA DE EXCEL: ")
    print('')
    global cpf
    entra = True
    cpf = input('Digite o número de CPF: ')
    while entra == True:
        if cpf == '00000000000':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '11111111111':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '22222222222':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '33333333333':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '44444444444':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '55555555555':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '66666666666':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '77777777777':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '88888888888':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        elif cpf == '99999999999':
            print('CPF INVALIDO!')
            cpf = input('Digite o número de CPF: ')
        try:
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            if re.search(r"^\d{11}$", cpf):
                if validar_cpf(cpf) == cpf:

                    entra = False
                else:
                    print("\nO numero {} é um numero de CPF invalido.\n".format(
                        cpf)
                    )
                    cpf = input('Digite o número de CPF: ')
            else:
                raise ValueError

        except ValueError:
            if cpf == '':
                print("Voce não informou o CPF!")
                cpf = input('Digite o número de CPF: ')

            elif re.search(r"^(\D+|\..*-_?)$", cpf):
                print("Informe apenas números!")
                cpf = input('Digite o número de CPF: ')
            else:
                print("Informe os 11 digitos do CPF!")
                cpf = input('Digite o número de CPF: ')
    validar_nome()
    global telefone
    telefone = input('Digite um número para contato: ')
    validar_segundo_celular()
    global celular
    celular = input('Digite um segundo número para contato  : ')
    validar_celular()
    global email
    email = input('Digite o E-mail do aluno: ')
    validar_email()
    alunosexcel[cpf] = [nome, telefone, celular, email]
    cpfsexcel.append(cpf)
    print("Matricula realizada com sucesso!")

def procurar_aluno_word():
    print('TURMA DE WORD')
    print("CPF: {}.{}.{}-{}".format(numcpf[0:3], numcpf[3:6],numcpf[6:9], numcpf[9:11]))
    print('Nome: ', alunosword[numcpf][0])
    formatar1 = alunosword[numcpf][1]
    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
    formatar = alunosword[numcpf][2]
    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
    print('E-mail: ', alunosword[numcpf][3])

def procurar_aluno_excel():
    print('TURMA DE EXCEL')
    print("CPF: {}.{}.{}-{}".format(numcpf[0:3], numcpf[3:6], numcpf[6:9], numcpf[9:11]))
    print('Nome: ', alunosexcel[numcpf][0])
    formatar1 = alunosexcel[numcpf][1]
    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
    formatar = alunosexcel[numcpf][2]
    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
    print('E-mail: ', alunosexcel[numcpf][3])

def procurar_aluno_powerpoint():
    print('TURMA DE POWER POINT')
    print("CPF: {}.{}.{}-{}".format(numcpf[0:3], numcpf[3:6], numcpf[6:9], numcpf[9:11]))
    print('Nome: ', alunospowerpoint[numcpf][0])
    formatar1 = alunospowerpoint[numcpf][1]
    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
    formatar = alunospowerpoint[numcpf][2]
    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
    print('E-mail: ', alunospowerpoint[numcpf][3])

def opcoes_editar():
    print('''1 - Editar aluno
2 - Lançar notas
3 - Editar notas
4 - Excluir aluno
5 - Notas''')

def dados_alunos():
    print('''1 - NOME
2 - CONTATO 1
3 - CONTATO 2
4 - E-MAIL''')





opcao = 0
#ler()
while opcao != '5':
    menu_inicial()
    opcao = input("Digite sua opção: ")
    if not opcao.isdigit():
        barra()
        print('{:^30}'.format('|Opção invalida|'))
        print('O VALOR DIGITADO NÃO É UM NÚMERO!')
        print('INFORME AO PROGRAMA UM VALOR ENTRE (1/4)')
        barra()
    elif opcao < '1' or opcao > '4':
        barra()
        print('{:^30}'.format('|Opção invalida|'))
        print('INFORME AO PROGRAMA UM VALOR ENTRE (1-4)')
        barra()


        opcao = 0

    elif opcao == '1':                                          #matriculaAluno
        turma()
        escolha = input('Escoha uma turma para matricular o aluno: ')
        while escolha < '1' or escolha > '3':
            barra()
            print("Opção invalida!")
            barra()
            escolha = input('Escoha uma turma para matricular o aluno: ')
        if escolha == '1':                                      #Matricular turma de word
            matricular_aluno_word()
        elif escolha == '2':                             #matricular turma de power point
            matricular_aluno_powerpoint()
        else:                                                        # matricular turma de excel
            matricular_aluno_excel()

        print()







    elif opcao == '2':                                                                               #EditarTurma
        turma()
        escolha = input('Digite o número da turma: ')                        #escolha
        while escolha != '1' and escolha != '2' and escolha != '3':
            barra()
            print('{:^30}'.format('|Opção invalida|'))
            print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
            barra()
            escolha = input('Digite o número da turma: ')            #Usuario define a turma

        if escolha == '1':                                              #Turma de word      #escolher_opção
            barra()
            print('TURMA DE WORD')
            print('-' * 40)
            opcoes_editar()
            barra()

            escolher_opcao = input('Digite uma opção: ')     #usuario escolhe entre editar aluno, editar notas, excluir aluno
            while escolher_opcao != '1' and escolher_opcao != '2' and escolher_opcao != '3' and escolher_opcao != '4' and escolher_opcao != '5':
                barra()
                print('{:^30}'.format('|Opção invalida|'))
                print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                barra()
                escolher_opcao = input('Digite uma opção: ')

            if escolher_opcao == '1':    #Editar aluno
                dados_alunos()                                                               #Escolha editar aluno
                escolha_editar_aluno = input("Digite uma das opções: ")
                while escolha_editar_aluno != '1' and escolha_editar_aluno != '2' and escolha_editar_aluno != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()

                    escolha_editar_aluno = input('Digite a opção que deseja editar: ')
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsword:
                        procurar_aluno_word()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                if escolha_editar_aluno == '1': #Editar nome
                    novonome = input('Digite o o nome do aluno: ')
                    aux = 1
                    while aux == 1:

                        if re.match("[^0-9][A-Za-z-ãõçóéúáí ]{3,}", novonome):
                            aux = 0
                        else:
                            print('Voçe digitou um caractere invalido!')
                            novonome = input('Digite o nome do aluno: ')

                    alunosword[numcpf][0] = novonome


                elif escolha_editar_aluno == '2': #Editar contato 1
                    novocontato1 = input('Contato - 1(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato1) != 11:
                                raise ValueError
                            else:
                                novocontato1 = int(novocontato1)  # se contiver letras causa um ValueError
                                novocontato1 = str(novocontato1)
                                numeroCelular = novocontato1

                                cont = False

                        except ValueError:
                            if len(novocontato1) == 0:
                                print('Você não digitou o número')
                                novocontato1 = input('Contato - 1(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato1 = input('Contato - 1(Atualizado): ')

                    alunosword[numcpf][1] = novocontato1

                elif escolha_editar_aluno == '3': #Editar contato 2
                    novocontato2 = input('Contato - 2(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato2) != 11:
                                raise ValueError
                            else:
                                novocontato2 = int(novocontato2)  # se contiver letras causa um ValueError
                                novocontato2 = str(novocontato2)
                                numeroCelular = novocontato2

                                cont = False

                        except ValueError:
                            if len(novocontato2) == 0:
                                print('Você não digitou o número')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                    alunosword[numcpf][2] = novocontato2

                elif escolha_editar_aluno == '4':              #Editar e-mail
                    email = input('E-mail(Atualizado): ')
                    validar = 1
                    while validar == 1:
                        if len(email) <= 5:
                            email = input('Digite o E-mail do aluno: ')
                        else:
                            if not '@' in email:
                                email = input('Digite o E-mail do aluno: ')
                            else:
                                if not email.endswith('.com'):
                                    email = input('Digite o E-mail do aluno: ')
                                else:
                                    validar = 0
                    alunosword[numcpf][3] = email


            elif escolher_opcao == '2':                #lançar notas

                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsword:
                        procurar_aluno_word()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                nota1 = float(input('Digite a nota 1: '))
                while nota1 < 0 or nota1 > 10:
                    print('informe um valor entre (1/10)')
                    nota1 = float(input('Digite a nota 1: '))
                nota2 = float(input('Digite a nota 2: '))
                while nota2 < 0 or nota2 > 10:
                    print('informe um valor entre (1/10)')
                    nota2 = float(input('Digite a nota 2: '))
                nota3 = float(input('Digite a nota 3: '))
                while nota3 < 0 or nota3 > 10:
                    print('informe um valor entre (1/10)')
                    nota3 = float(input('Digite a nota 3: '))
                media = (nota1 + nota2 + nota3)/3
                notasword[numcpf] = [nota1, nota2, nota3, media]
                barra()
                print('NOTAS NO SISTEMA!')
                barra()








            elif escolher_opcao == '3': #Editarnotas
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsword:
                        procurar_aluno_word()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('''1 - Nota(1)
2 - Nota(2)
3 - nota(3)''')
                escolher_nota_editar = input('Qual nota deseja editar: ')
                while escolher_nota_editar != '1' and escolher_nota_editar != '2' and escolher_nota_editar != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()
                if escolher_nota_editar == '1':
                    nota1novo = float(input('Digite a nota 1: '))
                    while nota1novo < 0 or nota1novo > 10:
                        print('informe um valor entre (1/10)')
                        nota1novo = float(input('Digite a nota 1: '))
                    notasword[numcpf][0] = [nota1novo]
                    media = (notasword[numcpf][0] + notasword[numcpf][1] + notasword[numcpf][2])/3
                    notasword[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota2novo = float(input('Digite a nota 2: '))
                    while nota2novo < 0 or nota2novo > 10:
                        print('informe um valor entre (1/10)')
                        nota2novo = float(input('Digite a nota 2: '))
                    notasword[numcpf][1] = [nota2novo]
                    media = (notasword[numcpf][0] + notasword[numcpf][1] + notasword[numcpf][2])/3
                    notasword[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota3novo = float(input('Digite a nota 1: '))
                    while nota3novo < 0 or nota3novo > 10:
                        print('informe um valor entre (1/10)')
                        nota3novo = float(input('Digite a nota 3: '))
                    notasword[numcpf][2] = [nota3novo]
                    media = (notasword[numcpf][0] + notasword[numcpf][1] + notasword[numcpf][2])/3
                    notasword[numcpf][3] = [media]
                print()
                print('Operação concluida!')


            elif escolher_opcao == '4':#Excluir aluno
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsword:
                        procurar_aluno_word()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                del alunosword[numcpf]
                del notasword[numcpf]
                for i, word in enumerate(cpfsword):
                    if word == numcpf:
                        del cpfsword[i]
                barra()
                print('ALUNO EXCLUIDO DO SISTEMA')
                barra()


            else:
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsword:
                        procurar_aluno_word()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('Nota - 1: {}'.format(notasword[numcpf][0]))
                print('Nota - 2: {}'.format(notasword[numcpf][1]))
                print('Nota - 3: {}'.format(notasword[numcpf][2]))
                print('Média: {}'.format(notasword[numcpf][3]))
                if notasword[numcpf][3] >= 7:
                    barra()
                    print('ALUNO APROVADO!')
                    barra()
                else:
                    barra()
                    print('ALUNO REPROVADO!')
                    barra()







        elif escolha == '2':                                                #Turma de power point
            barra()
            print('TURMA DE POWER POINT')
            print('-' * 40)
            opcoes_editar()
            barra()
            escolher_opcao = input('Digite uma opção: ')  # usuario escolhe entre editar aluno, editar notas, excluir aluno
            while escolher_opcao != '1' and escolher_opcao != '2' and escolher_opcao != '3' and escolher_opcao != '4' and escolher_opcao != '5':
                barra()
                print('{:^30}'.format('|Opção invalida|'))
                print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                barra()
                escolher_opcao = input('Digite uma opção: ')

            if escolher_opcao == '1':  # Editar aluno
                dados_alunos()  # Escolha editar aluno
                escolha_editar_aluno = input("Digite uma das opções: ")
                while escolha_editar_aluno != '1' and escolha_editar_aluno != '2' and escolha_editar_aluno != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()

                    escolha_editar_aluno = input('Digite a opção que deseja editar: ')
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfspowerpoint:
                        procurar_aluno_powerpoint()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                if escolha_editar_aluno == '1':  # Editar nome
                    novonome = input('Digite o o nome do aluno: ')
                    aux = 1
                    while aux == 1:

                        if re.match("[^0-9][A-Za-z-ãõçóéúáí ]{3,}", novonome):
                            aux = 0
                        else:
                            print('Voçe digitou um caractere invalido!')
                            novonome = input('Digite o nome do aluno: ')
                    alunospowerpoint[numcpf][0] = novonome

                elif escolha_editar_aluno == '2':  # Editar contato 1
                    novocontato1 = input('Contato - 1(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato1) != 11:
                                raise ValueError
                            else:
                                novocontato1 = int(novocontato1)  # se contiver letras causa um ValueError
                                novocontato1 = str(novocontato1)
                                numeroCelular = novocontato1

                                cont = False

                        except ValueError:
                            if len(novocontato1) == 0:
                                print('Você não digitou o número')
                                novocontato1 = input('Contato - 1(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato1 = input('Contato - 1(Atualizado): ')

                    alunospowerpoint[numcpf][1] = novocontato1

                elif escolha_editar_aluno == '3':  # Editar contato 2
                    novocontato2 = input('Contato - 2(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato2) != 11:
                                raise ValueError
                            else:
                                novocontato2 = int(novocontato2)  # se contiver letras causa um ValueError
                                novocontato2 = str(novocontato2)
                                numeroCelular = novocontato2

                                cont = False

                        except ValueError:
                            if len(novocontato2) == 0:
                                print('Você não digitou o número')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                    alunospowerpoint[numcpf][2] = novocontato2

                elif escolha_editar_aluno == '4':  # Editar e-mail
                    email = input('E-mail(Atualizado): ')
                    validar = 1
                    while validar == 1:
                        if len(email) <= 5:
                            email = input('Digite o E-mail do aluno: ')
                        else:
                            if not '@' in email:
                                email = input('Digite o E-mail do aluno: ')
                            else:
                                if not email.endswith('.com'):
                                    email = input('Digite o E-mail do aluno: ')
                                else:
                                    validar = 0
                    alunospowerpoint[numcpf][3] = email



            elif escolher_opcao == '2':                                                     # Lançar notas
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfspowerpoint:
                        procurar_aluno_powerpoint()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                nota1 = float(input('Digite a nota 1: '))
                while nota1 < 0 or nota1 > 10:
                    print('informe um valor entre (1/10)')
                    nota1 = float(input('Digite a nota 1: '))
                nota2 = float(input('Digite a nota 2: '))
                while nota2 < 0 or nota2 > 10:
                    print('informe um valor entre (1/10)')
                    nota2 = float(input('Digite a nota 2: '))
                nota3 = float(input('Digite a nota 3: '))
                while nota3 < 0 or nota3 > 10:
                    print('informe um valor entre (1/10)')
                    nota3 = float(input('Digite a nota 3: '))
                media = (nota1 + nota2 + nota3) / 3
                notaspowerpoint[numcpf] = [nota1, nota2, nota3, media]
                barra()
                print('NOTAS NO SISTEMA!')
                barra()



            elif escolher_opcao == '3':                        #Editar notas
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfspowerpoint:
                        procurar_aluno_powerpoint()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('''1 - Nota(1)
                2 - Nota(2)
                3 - nota(3)''')
                escolher_nota_editar = input('Qual nota deseja editar: ')
                while escolher_nota_editar != '1' and escolher_nota_editar != '2' and escolher_nota_editar != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()
                if escolher_nota_editar == '1':
                    nota1novo = float(input('Digite a nota 1: '))
                    while nota1novo < 0 or nota1novo > 10:
                        print('informe um valor entre (1/10)')
                        nota1novo = float(input('Digite a nota 1: '))
                    notaspowerpoint[numcpf][0] = [nota1novo]
                    media = (notaspowerpoint[numcpf][0] + notaspowerpoint[numcpf][1] + notaspowerpoint[numcpf][2]) / 3
                    notaspowerpoint[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota2novo = float(input('Digite a nota 2: '))
                    while nota2novo < 0 or nota2novo > 10:
                        print('informe um valor entre (1/10)')
                        nota2novo = float(input('Digite a nota 2: '))
                    notaspowerpoint[numcpf][1] = [nota2novo]
                    media = (notaspowerpoint[numcpf][0] + notaspowerpoint[numcpf][1] + notaspowerpoint[numcpf][2]) / 3
                    notaspowerpoint[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota3novo = float(input('Digite a nota 1: '))
                    while nota3novo < 0 or nota3novo > 10:
                        print('informe um valor entre (1/10)')
                        nota3novo = float(input('Digite a nota 3: '))
                    notaspowerpoint[numcpf][2] = [nota3novo]
                    media = (notaspowerpoint[numcpf][0] + notaspowerpoint[numcpf][1] + notaspowerpoint[numcpf][2]) / 3
                    notaspowerpoint[numcpf][3] = [media]
                print()
                print('Operação concluida!')


            elif escolher_opcao == '4':                                              #Excluir aluno
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfspowerpoint:
                        procurar_aluno_powerpoint()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                del alunospowerpoint[numcpf]
                del notaspowerpoint[numcpf]
                for i, word in enumerate(cpfspowerpoint):
                    if word == numcpf:
                        del cpfspowerpoint[i]
                barra()
                print('ALUNO EXCLUIDO DO SISTEMA')
                barra()

            else:                               #ver notas/ status
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfspowerpoint:
                        procurar_aluno_powerpoint()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('Nota - 1: {}'.format(notaspowerpoint[numcpf][0]))
                print('Nota - 2: {}'.format(notaspowerpoint[numcpf][1]))
                print('Nota - 3: {}'.format(notaspowerpoint[numcpf][2]))
                print('Média: {}'.format(notaspowerpoint[numcpf][3]))
                if notaspowerpoint[numcpf][3] >= 7:
                    barra()
                    print('ALUNO APROVADO!')
                    barra()
                else:
                    barra()
                    print('ALUNO REPROVADO!')
                    barra()





        elif escolha == '3':  #Turma de excel
            barra()
            print('TURMA DE EXCEL')
            print('-' * 40)
            opcoes_editar()
            barra()
            escolher_opcao = input('Digite uma opção: ')
            while escolher_opcao != '1' and escolher_opcao != '2' and escolher_opcao != '3':
                barra()
                print('{:^30}'.format('|Opção invalida|'))
                print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                barra()
                escolher_opcao = input('Digite uma opção: ')

            if escolher_opcao == '1':  # Editar aluno
                dados_alunos()  # Escolha editar aluno
                escolha_editar_aluno = input("Digite uma das opções: ")
                while escolha_editar_aluno != '1' and escolha_editar_aluno != '2' and escolha_editar_aluno != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()

                    escolha_editar_aluno = input('Digite a opção que deseja editar: ')
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsexcel:
                        procurar_aluno_excel()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                if escolha_editar_aluno == '1':  # Editar nome
                    novonome = input('Digite o o nome do aluno: ')
                    novonome = input('Digite o o nome do aluno: ')
                    aux = 1
                    while aux == 1:

                        if re.match("[^0-9][A-Za-z-ãõçóéúáí ]{3,}", novonome):
                            aux = 0
                        else:
                            print('Voçe digitou um caractere invalido!')
                            novonome = input('Digite o nome do aluno: ')
                    alunosexcel[numcpf][0] = novonome

                elif escolha_editar_aluno == '2':  # Editar contato 1
                    novocontato1 = input('Contato - 1(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato1) != 11:
                                raise ValueError
                            else:
                                novocontato1 = int(novocontato1)  # se contiver letras causa um ValueError
                                novocontato1 = str(novocontato1)
                                numeroCelular = novocontato1

                                cont = False

                        except ValueError:
                            if len(novocontato1) == 0:
                                print('Você não digitou o número')
                                novocontato1 = input('Contato - 1(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato1 = input('Contato - 1(Atualizado): ')

                    alunosexcel[numcpf][1] = novocontato1

                elif escolha_editar_aluno == '3':  # Editar contato 2
                    novocontato2 = input('Contato - 2(Atualizado): ')
                    cont = True

                    while cont == True:
                        try:
                            if len(novocontato2) != 11:
                                raise ValueError
                            else:
                                novocontato2 = int(novocontato2)  # se contiver letras causa um ValueError
                                novocontato2 = str(novocontato2)
                                numeroCelular = novocontato2

                                cont = False

                        except ValueError:
                            if len(novocontato2) == 0:
                                print('Você não digitou o número')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                            else:
                                print('Número inválido, o número precisa ter 11 números inteiros')
                                novocontato2 = input('Contato - 2(Atualizado): ')
                    alunosexcel[numcpf][2] = novocontato2

                elif escolha_editar_aluno == '4':  # Editar e-mail
                    email = input('E-mail(Atualizado): ')
                    validar = 1
                    while validar == 1:
                        if len(email) <= 5:
                            email = input('Digite o E-mail do aluno: ')
                        else:
                            if not '@' in email:
                                email = input('Digite o E-mail do aluno: ')
                            else:
                                if not email.endswith('.com'):
                                    email = input('Digite o E-mail do aluno: ')
                                else:
                                    validar = 0
                    alunosexcel[numcpf][3] = email



            elif escolher_opcao == '2':                                                     # Lançar notas
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsexcel:
                        procurar_aluno_excel()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)

                nota1 = float(input('Digite a nota 1: '))
                while nota1 < 0 or nota1 > 10:
                    print('informe um valor entre (1/10)')
                    nota1 = float(input('Digite a nota 1: '))
                nota2 = float(input('Digite a nota 2: '))
                while nota2 < 0 or nota2 > 10:
                    print('informe um valor entre (1/10)')
                    nota2 = float(input('Digite a nota 2: '))
                nota3 = float(input('Digite a nota 3: '))
                while nota3 < 0 or nota3 > 10:
                    print('informe um valor entre (1/10)')
                    nota3 = float(input('Digite a nota 3: '))
                media = (nota1 + nota2 + nota3) / 3
                notasexcel[numcpf] = [nota1, nota2, nota3, media]
                barra()
                print('NOTAS NO SISTEMA!')
                barra()



            elif escolher_opcao == '3':                        #Editar notas
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsexcel:
                        procurar_aluno_excel()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('''1 - Nota(1)
                2 - Nota(2)
                3 - nota(3)''')
                escolher_nota_editar = input('Qual nota deseja editar: ')
                while escolher_nota_editar != '1' and escolher_nota_editar != '2' and escolher_nota_editar != '3':
                    barra()
                    print('{:^30}'.format('|Opção invalida|'))
                    print('INFORME AO PROGRAMA UM VALOR ENTRE (1-3)')
                    barra()
                if escolher_nota_editar == '1':
                    nota1novo = float(input('Digite a nota 1: '))
                    while nota1novo < 0 or nota1novo > 10:
                        print('informe um valor entre (1/10)')
                        nota1novo = float(input('Digite a nota 1: '))
                    notasexcel[numcpf][0] = [nota1novo]
                    media = (notasexcel[numcpf][0] + notasexcel[numcpf][1] + notasexcel[numcpf][2]) / 3
                    notasexcel[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota2novo = float(input('Digite a nota 2: '))
                    while nota2novo < 0 or nota2novo > 10:
                        print('informe um valor entre (1/10)')
                        nota2novo = float(input('Digite a nota 2: '))
                    notasexcel[numcpf][1] = [nota2novo]
                    media = (notasexcel[numcpf][0] + notasexcel[numcpf][1] + notasexcel[numcpf][2]) / 3
                    notasexcel[numcpf][3] = [media]
                if escolher_nota_editar == '1':
                    nota3novo = float(input('Digite a nota 1: '))
                    while nota3novo < 0 or nota3novo > 10:
                        print('informe um valor entre (1/10)')
                        nota3novo = float(input('Digite a nota 3: '))
                    notasexcel[numcpf][2] = [nota3novo]
                    media = (notasexcel[numcpf][0] + notasexcel[numcpf][1] + notasexcel[numcpf][2]) / 3
                    notasexcel[numcpf][3] = [media]
                print()
                print('Operação concluida!')


            elif escolher_opcao == '4':                                              #Excluir aluno
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsexcel:
                        procurar_aluno_excel()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                del alunosexcel[numcpf]
                del notasexcel[numcpf]
                for i, word in enumerate(cpfsexcel):
                    if word == numcpf:
                        del cpfsexcel[i]
                barra()
                print('ALUNO EXCLUIDO DO SISTEMA')
                barra()

            else:                               #ver notas/ status
                cont = 1
                while cont == 1:
                    numcpf = input('Digite o CPF do Aluno: ')
                    if numcpf in cpfsexcel:
                        procurar_aluno_excel()
                        cont = 0
                    else:
                        print('-' * 40)
                        print('ALUNO NÃO ENCONTRADO!')
                        print('-' * 40)
                print('Nota - 1: {}'.format(notasexcel[numcpf][0]))
                print('Nota - 2: {}'.format(notasexcel[numcpf][1]))
                print('Nota - 3: {}'.format(notasexcel[numcpf][2]))
                print('Média: {}'.format(notasexcel[numcpf][3]))
                if notasexcel[numcpf][3] >= 7:
                    barra()
                    print('ALUNO APROVADO!')
                    barra()
                else:
                    barra()
                    print('ALUNO REPROVADO!')
                    barra()







    elif opcao == '3':                              #Procurar aluno

        print('''1- Buscar Aluno
2- Buscar Turma''')
        aux1 = input('Escolha uma opção: ')
        while aux1 <'1' or aux1>'2':
            barra()
            print('Opção Inválida')
            barra()
            aux1 = input('Escolha uma opção: ')
        if aux1 =='1':

            cont = 1

            while cont == 1:
                numcpf = input('Digite o CPF do aluno: ')
                if numcpf in cpfsword:
                    procurar_aluno_word()
                    cont = 0
                elif numcpf in cpfspowerpoint:
                    procurar_aluno_powerpoint()
                    cont = 0
                elif numcpf in alunosexcel:
                    procurar_aluno_excel()
                    cont = 0

                else:
                    print('-' * 40)
                    print('ALUNO NÃO ENCONTRADO!')
                    print('-' * 40)
        else:
            turma()

            escolhe_turma = input('Digite o número da turma que deseja recuperar: ')
            while escolhe_turma <'1' or escolhe_turma >'3':
                barra()
                print('Opção Inválida!')
                barra()
                escolhe_turma = input('Digite o número da turma que deseja recuperar: ')

            cont = 1
            if escolhe_turma == '1':
                print('TURMA DE WORD')
                for i in cpfsword:
                    print("CPF: {}.{}.{}-{}".format(i[0:3], i[3:6], i[6:9], i[9:11]))
                    print('Nome: ', alunosword[i][0])
                    formatar1 = alunosword[i][1]
                    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
                    formatar = alunosword[i][2]
                    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
                    print('E-mail: ', alunosword[i][3])
                    print('-' * 40)

            elif escolhe_turma =='2':
                print('TURMA DE POWER POINT')
                for x in cpfspowerpoint:
                    print("CPF: {}.{}.{}-{}".format(x[0:3], x[3:6], x[6:9], x[9:11]))
                    print('Nome: ', alunospowerpoint[x][0])
                    formatar1 = alunospowerpoint[x][1]
                    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
                    formatar = alunospowerpoint[x][2]
                    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
                    print('E-mail: ', alunospowerpoint[x][3])
                    print('-' * 40)

            else:
                print('TURMA DE EXCEL')
                for y in cpfsexcel:
                    print("CPF: {}.{}.{}-{}".format(y[0:3], y[3:6], y[6:9], y[9:11]))
                    print('Nome: ', alunosexcel[y][0])
                    formatar1 = alunosexcel[y][1]
                    print('Contato - 1: ({}) {}-{}-{}'.format(formatar1[0:2], formatar1[2], formatar1[3:7], formatar1[7:]))
                    formatar = alunosexcel[y][2]
                    print('Contato - 2: ({}) {}-{}-{}'.format(formatar[0:2], formatar[2], formatar[3:7], formatar[7:]))
                    print('E-mail: ', alunosexcel[y][3])
                    print('-' * 40)










    else:
        opcao = '5'
        barra()
        print('Fim do programa!')
        barra()
        #salvar()




