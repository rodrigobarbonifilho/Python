# coding=utf-8
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))  # valores atribuidos
v3 = int(input('Terceiro valor: '))

listinha = [v1, v2, v3]               # lista para ver qual é amior e qual e menor

print('\033[34mo menor valor digitado foi {}'.format(min(listinha)))
print('O maio valor digitado foi {}\033[m'.format(max(listinha)))

# jeito cheio de if's
print()

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))  # valores atribuidos
v3 = int(input('Terceiro valor: '))

if v1 < v2 and v1 < v3:
    print('O menor valor digitado foi {}'.format(v1))
if v2 < v1 and v2 < v3:
    print('O maior valor digitado foi {}'.format(v2))  # menor valor
if v3 < v1 and v3 < v2:
    print('O maior valor digitado foi {}'.format(v3))

if v1 > v2 and v1 > v3:
    print('O maior valor digitado foi {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O maior valor digitado foi {}'.format(v2))   # maior valor
if v3 > v1 and v3 > v2:
    print('O maior valor digitado foi {}'.format(v3))
else:
    print('Valor nao encontrado')
