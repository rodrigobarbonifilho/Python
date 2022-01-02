"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
"""

# Criar a lista
lista = []

# Receber valores
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N]: ').strip()[0]
    while resp not in 'NnSs':
        resp = input('Quer continuar? [S/N]: ').strip()[0]
    if resp in 'Nn':
        break

print('-=' * 30)

# A) Quantos números foram digitados.
print(f'Você digitou {len(lista)} elementos')

# B) A lista de valores, ordenada de forma decrescente.
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')

# C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
