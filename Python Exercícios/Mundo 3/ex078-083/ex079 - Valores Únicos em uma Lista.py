"""
Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma 'lista'.
Caso o numero já exista lá dentro, ele 'não será adicionado'.
No final, serão exibidos todos 'valores unicos' digitados, em 'ordem crescente'.
"""
# Criar lista
valores = list()
resp = ''

# Adicionar valores a lista (verificando se noa estao duplicados
while resp != 'N':
    n = int(input('\033[1;31mDigite um valor:\033m '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    resp = input('Quer continuar? [S/N]: ').upper()[0]
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N]: ').upper()[0]
print(30*'-=')

# E no final mostrar os numeros unicos
valores.sort()
print(f'Os numeros digitado foram: {str(valores).replace("[", "").replace("]", "")}')
