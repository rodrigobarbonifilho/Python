# A estrutura break interrompe as iterações while e for
# Estrutura infinita
cont = 1
while True:
    print(cont, ' -> ', end='')
    cont += 1
    if cont == 10:
        break

# Estrutura usando o break
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

# F-string
nome = 'Joao'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}!')  # Que é igual a =
print('O {} tem {} anos e ganha {}!'.format(nome, idade, salario))  # Que é igual a =
print('O %s tem %i anos e ganha %s!' % (nome, idade, salario))
