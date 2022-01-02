cores = ('\033[m',      # 0 - Sem Cor
         '\033[30m',    # 1 - Branco
         '\033[31m',    # 2 - Vermelho
         '\033[33m',    # 3 - Amarelo
         '\033[34m')    # 4 - Azul


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
