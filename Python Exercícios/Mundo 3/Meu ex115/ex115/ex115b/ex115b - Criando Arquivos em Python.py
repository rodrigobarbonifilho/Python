from ex115.ex115b.dados import *
from time import sleep

while True:
    titulo('MENU PRINCIPAL', 50, 4)
    print("""\033[33m1 - \033[34mVer pessoas cadastradas
\033[33m2 - \033[34mCadastrar nova pessoa
\033[33m3 - \033[34mSair do Sistema\033[m""")
    print('-' * 50)
    esc = leiaInt('\033[33mSua Opção: \033[m')
    if esc > 3 or esc < 0:
        print('\033[31mERRO! Digite um numero correspondente!\033[m')
        sleep(0.5)
        continue
    else:
        if esc == 1:
            titulo('PESSOAS CADASTRADAS', 50)
            escrever_arquivo('cursoemvideo.txt')
        elif esc == 2:
            titulo('NOVO CADASTRO', 50)
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrar_pessoa(nome, idade)
        elif esc == 3:
            titulo('Saindo...', 50)
            sleep(1)
            print(f'{"<"*20:<20}{" Até logo ".center(10)}{">"*20:>20}')
            break
