from ex115b.interface import *
from time import sleep

text = 'cursoemvideo.txt'

criarArquivo(text)

while True:
    resposta = menu(['Mostrar pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])

    if resposta == 1:
        leiaArquivo(text)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar(text, nome, idade)
    elif resposta == 3:
        print(linha())
        print('Saindo do Sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Por favor digite um número válido!\033[m')
    sleep(1)
