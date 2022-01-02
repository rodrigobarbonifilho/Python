def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt=''):
    print(linha())
    print(f'{str(txt):^42}')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[33mSua opção: \033[m')
    return opc


def criarArquivo(txt='textodepython'):
    try:
        a = open(txt, 'r')
        a.close()
    except FileNotFoundError:
        a = open(txt, 'w')
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {txt} criado com sucesso!')


def leiaArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na leitura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            a.close()
        except:
            print('Houve um ERRO na digitação do arquivo')
        else:
            print(f'Arquivo de {nome} cadastrada com sucesso')
