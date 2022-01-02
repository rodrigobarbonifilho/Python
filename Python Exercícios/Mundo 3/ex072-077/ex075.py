# Fazer um programa que leia quatro numeros pelo teclado e coloque numa tupla
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
n3 = int(input('Digite so mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
np = 0
numeros = (n1, n2, n3, n4)
for n in numeros:
    if n % 2 == 0:
        np += 1
print(f'Voce digitou os numeros: {numeros}')
print(10*'--', 'Dados', 10*'--')

# a) Quantas vezes apareceu o numero 9
if numeros.count(9) == 0:
    print('O número 9 nao apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {numeros.count(9)} vez(es)')

# b) Em que posiçao apareceu o primeiro valor 3
if numeros.count(3) == 0:
    print('Nao foi digitado o número 3')
else:
    print(f'O número 3 apareceu pela primeira vez na {numeros.index(3)+1}ª posição')

# c) Quais foram os numero pares
if np == 0:
    print('Nao foi digitado nenhum numero par')
else:
    print('Os numeros pares digitado foi: ', end='')
    for n in numeros:
        if n % 2 == 0:
            print(n, end=' ')
