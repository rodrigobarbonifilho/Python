# coding=utf-8
import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo  aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quato    aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('\033[1;36ma ordem das apresentações do trabalho será: {}, {}, {}, {}\033[m'.format(lista[0], lista[1], lista[2], lista[3]))
