from ex115a import dados
from time import sleep

while True:
    dados.titulo('MENU PRINCIPAL', 50, 4)
    print("""\033[33m1 - \033[34mVer pessoas cadastradas
\033[33m2 - \033[34mCadastrar nova pessoa
\033[33m3 - \033[34mSair do Sistema\033[m""")
    print('-' * 50)
    esc = dados.leiaInt('\033[33mSua Opção: \033[m')
    if esc > 3 or esc < 0:
        print('\033[31mERRO! Digite um numero correspondente!\033[m')
        sleep(0.5)
        continue
    else:
        if esc == 1:
            dados.titulo('Opção 1', 50)
        elif esc == 2:
            dados.titulo('Opção 2', 50)
        elif esc == 3:
            dados.titulo('Opção 3', 50)
            break
