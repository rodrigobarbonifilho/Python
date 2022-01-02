from ex115a.interface import *
from time import sleep

while True:
    resposta = menu(['Mostrar pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        print('Saindo do Sistema... Até logo')
        break
    else:
        linha()
        print('\033[31mERRO! Por favor digite um número válido!\033[m')
    sleep(1)
