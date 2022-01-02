cores = ('\033[m',      # 0 - Sem Cor
         '\033[30m',    # 1 - Branco
         '\033[31m',    # 2 - Vermelho
         '\033[33m',    # 3 - Amarelo
         '\033[34m')    # 4 - Azul


def escrever_arquivo(txt='textodepython.txt'):
    try:
        texto = open(txt, 'r')
    except FileNotFoundError:
        open(txt, 'w')
    else:
        lista = list()
        for l in texto:
            lista.append(l.replace('\n', '').split(';'))
        for p, d in enumerate(lista):
            print(f'{lista[p][0]:<35}{lista[p][1]:>10} anos')


def cadastrar_pessoa(nome, idade, texto='cursoemvideo.txt'):
    texto = open(texto, 'a')
    texto.write(f'{nome};{idade}\n')
    texto.close()


def leiaInt(msg):
    while True:
        try:
            global n
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um valor inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO! É necessário informar um número inteiro de 1 a 3!')
        else:
            return n


def titulo(tit='', tam=0, c=0):
    print('-' * tam)
    try:
        print(cores[c], tit.center(tam), cores[0])
    except IndexError:
        print('Cor Ínvalida!')
    print('-' * tam)
