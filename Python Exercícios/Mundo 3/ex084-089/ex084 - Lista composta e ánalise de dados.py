"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:"""
print('-=' * 30)
pessoas = []
dados = []
resp = ''
cont = 0

while True:
    nome = input('Nome: ').strip().lower().capitalize()  # Pegando nome
    peso = float(input('Peso: [Kg] '))  # Pegando peso
    print('-=' * 30)

    if cont == 0:
        maip = menp = peso
    else:
        if peso > maip:
            maip = peso
        if peso < menp:
            menp = peso
    cont += 1

    dados.append(nome)  # Adicionando nome em dados
    dados.append(peso)  # Adicionando peso em dados
    pessoas.append(dados[:])  # Jogando tudo numa lista composta
    dados.clear()  # Limpando a lista temporaria
    
    resp = input('Deseja continuar? [S/N]: ').strip()[0]  # Perguntando se deseja continuar

    print('-=' * 30)
    
    while resp not in 'SsNn':  # Verificando resposta
        resp = input('Tente novamente. Deseja continuar? [S/N]: ')
    
    if resp in 'Nn':  # Interrompendo a iteração
        break

# A) Quantas pessoas foram cadastradas.
print(f'Foi cadastrado {len(pessoas)} pessoas!')

# B) Uma listagem com as pessoas mais pesadas.
print(f'O maior peso foi de {maip}. Peso de: ', end='')
for p in pessoas:
    if p[1] == maip:
        print(f'{p[0]}', end='... ')

# C) Uma listagem com as pessoas mais leves.
print(f'\nO menor peso foi de {menp}. Peso de: ', end='')
for p in pessoas:
    if p[1] == menp:
        print(f'{p[0]}', end='... ')

print()

print('-=' * 30)
