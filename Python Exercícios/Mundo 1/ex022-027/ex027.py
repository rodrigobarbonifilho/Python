# coding=utf-8
nome = input('Qual seu nome completo? ').split()

print()

print('\033[34mPrazer em te conhecer.')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome e: {}\033[m'.format(nome[-1]))
