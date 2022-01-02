# Variaveis Compostas
lista_de_cadastrados = []
ficha = {
    'nome': '', 
    'idade': 0, 
    'sexo': ''
}

# Variaveis
media = 0

print('-=' * 30)

# Validando e colocando os dados no dicionário
while True:
    ficha['nome'] = input('Nome: ').strip().capitalize()
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Responda apenas F ou M.')
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    ficha['sexo'] = sexo
    ficha['idade'] = int(input('Idade: '))
    
    lista_de_cadastrados.append(ficha.copy())

    resp = input('Quer continuar? [S/N]: ').strip()[0]
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N]: ')
    print('-=' * 30)
    if resp in 'Nn':
        break

# A) Ao todo quantas pessoas foram cadastradas
print(f'A) Ao todo temos {len(lista_de_cadastrados)} pessoas cadastradas.')

# B) A média de idade das pessoas cadastradas
for d in lista_de_cadastrados:
    for k, v in d.items():
        if k == 'idade':
            media += v
media /= len(lista_de_cadastrados)
print(f'B) A média de idade é de: {media:.2f} anos.')

# C) Mostrar as mulheres cadastradas
print(f'C) As mulheres cadastradas foram: ', end='')
for d in lista_de_cadastrados:
    if d['sexo'] == 'f' or d['sexo'] == 'F':
        print(d['nome'], end=' ')
print()

# D) Lista das pessoas que estão acima da média
print('D) Lista de pessoas que estão acima da média:')
for d in lista_de_cadastrados:
    if d['idade'] > media:
        print('     ', end='')
        for k, v in d.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<< Volte Sempre >>')
