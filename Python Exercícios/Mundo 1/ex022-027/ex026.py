# coding=utf-8
frase = input('Digite uma frase: ').strip().upper()

print('\033[36mA letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na {} posição'.format(frase.find('A')+1))
print('A ultima letra A aparece na {} posição\033[m'.format(frase.rfind('A')+1))
