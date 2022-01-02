from random import choice

lista = []

aluno1 = input('Primerio aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

# Poderia ter feito assim --> [n1, n2, n3,n4]

lista.extend((aluno1, aluno2, aluno3, aluno4))

print()

print('\033[1;31mO aluno escolhido foi:{}\033[m'.format(choice(lista)))
