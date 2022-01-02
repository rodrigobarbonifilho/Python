from time import sleep


c = ('\033[m',       # 0 - Sem cor
     '\033[1;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7;30m'       # 6 - Branco
    )


def Escreva(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')


def ajuda(fun):
    sleep(1)
    Escreva(f'Acessando o manual do comando {fun}', 4)
    sleep(1)
    print(c[6], end='')
    return help(fun)
    print(c[0], end='')


# Programa principal
while True:
    Escreva('SISTEMA DE AJUDA PyHELP', 2)
    f = input('Biblioteca ou Função > ').strip()
    if f.upper() in 'FIM':
        sleep(1)
        Escreva('ATÉ LOGO', 1)
        sleep(1)
        break
    ajuda(f)
