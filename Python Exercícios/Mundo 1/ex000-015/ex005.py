# coding=utf-8
n1 = int(input('Coloque um numero:'))
sucessor = n1 + 1
antecessor = n1 - 1
print('\033[1;35mAnalisando o valor {} temos que...\033[m'.format(n1))
print('\033[1;34mSeu sucessor é:{}'.format(sucessor))
print('Seu antecessor é:{}\033[m'.format(antecessor))
