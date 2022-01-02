sexo = input('Digite seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dado Invalido! Digite seu sexo corretamente, por favor: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
