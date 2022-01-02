from datetime import date
ano = date.today().year
sexo = input('Qual o seu genero."F" para feminino e "M" para masculino: ').lower().strip()
if sexo == 'feminino' or sexo == 'f':
    print('Voce nao precisa se alistar!')
    print()
    print('Mas se quiser se alistar digite:')
    print('[ 1 ] Para se alistar;')
    print('[ 2 ] Para nao se alistar.')
    escolha = input('Sua opção: ')
    print()
    if escolha == '1':
        nascimento = int(input('Ano de nascimento: '))
        idade = ano - nascimento
        print()
        print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))
        if idade < 18:
            tempo = 18 - idade
            alistamento = ano + tempo
            print('\033[1;32mAinda faltam {} ano(s) para o seu alistamento!'.format(tempo))
            print('Seu alistamento será em {}\033[m'.format(alistamento))
        elif idade == 18:
            print('\033[1;33mVoce tem que se alistar IMEDIATAMENTE!\033[m')
        elif idade > 18:
            tempo = idade - 18
            alistamento = ano - tempo
            print('\033[1;31mVoce deveria ter se alistado há {} ano(s)!'.format(tempo))
            print('Seu alistamento foi em {}\033[m'.format(alistamento))
    elif escolha == '2':
        print('\033[1;36mEsta bem\033[m')
    else:
        print('\033[1;31mNumero Invalido. Tente novamente!\033[m')
elif sexo == 'masculino' or sexo == 'm':
    nascimento = int(input('Ano de nascimento: '))
    idade = ano - nascimento
    print()
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))
    if idade < 18:
        tempo = 18 - idade
        alistamento = ano + tempo
        print('\033[1;32mAinda faltam {} ano(s) para o seu alistamento!'.format(tempo))
        print('Seu alistamento será em {}\033[m'.format(alistamento))
    elif idade == 18:
        print('\033[1;33mVoce tem que se alistar IMEDIATAMENTE!\033[m')
    elif idade > 18:
        tempo = idade - 18
        alistamento = ano - tempo
        print('\033[1;31mVoce deveria ter se alistado há {} ano(s)!'.format(tempo))
        print('Seu alistamento foi em {}\033[m'.format(alistamento))
else:
    print('\033[1;31mGenero invalido!\033[m')
