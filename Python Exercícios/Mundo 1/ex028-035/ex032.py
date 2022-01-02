# coding=utf-8
from datetime import date
from time import sleep

print(20 * '\033[1;34m-=-')
print('\033[1;33mOi irei analisar um ano e verei se ele BISSEXTO ou não.')
print(20 * '\033[1;34m-=-')
ano = int(input('\033[1;35mQual ano você quer analisar? Digite 0 para analisar o ano atual: \033[m'))

print('Analisando...')
sleep(1)
print('Fazendo calculos...')
sleep(1)
print('Pronto...')
sleep(0.50)
print()

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano e bissexto!')
else:
    print('Este ano nao foi bissexto!')
