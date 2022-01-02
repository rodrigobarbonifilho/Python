# coding=utf-8
nome = input('Coloque aqui seu nome completo: ')
primeiro_nome = nome.split()

print()

print('\033[1;36mAnalisando seu nome,podemos ver que...')
print('Seu nome completo todo em Maisculo é: {}'.format(nome.upper()))
print('Seu nome completo tofo em Minusculo é: {}'.format(nome.lower()))
print('Seu nome ao todo tem: {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem: {} letras\033[m'.format(len(primeiro_nome[0])))
