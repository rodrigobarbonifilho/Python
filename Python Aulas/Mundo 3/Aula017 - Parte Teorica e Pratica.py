# ============================================ LISTAS 1 ==============================================
# Digamos que precisasse organizar os seguintes itens: hamburguer, suco, pizza, pudim
# Usando a tupla fariamos assim:
#    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# E dermos o comando:
#    print(lanche[2]) # Que daria 'pizza'
# Resultado:
#    'pizza'
#
# E se dermos:
#    lanche[3] = 'picole'
# Resultado:
#    Erro: TypeError: 'tuple' object does not support item assignment
#
# Para poder fazer o seguinte codigo funcionar:
#    lanche[3] = 'picole'
# Necessitariamos de usar as Listas:
#    Tuplas = () (feita por parenteses)
#    Listas = [] (feita por colchetes)
#
# ================================= Diferenças entre TUPLAS e LISTAS ==================================
# Então se eu fizer:
#    lanche = ['hambuerguer', 'suco', 'pizza', 'pudim']
# E depois executar o comando:
#    lanche[3] = 'picole'
# Acontecerá que o 'pudim' será substitoido por 'picole' e ao executarmos o comando:
#    print(lanche)
# A saída será:
#    ['hamburguer', 'suco', 'pizza', 'picole'] # Pois as Listas são mutáveis
#
# ====================================== Usando o metodo APPEND() =====================================
# Na tupla eu não poderia adicionar mais alimentos já na lista podemos usando o comando:
#    lanche.append('cookie')
# E ao darmos:
#    print(lanche)
# A saída seria:
#    ['hamburguer', 'suco', 'pizza', 'picole', 'cookie']
#
# ====================================== Usando o metodo INSERT() =====================================
# Poderiamos usar o insert() tambem para adiciornarmos itens em indices escolhidos:
# Ex:
#    lanche.insert(0, 'cachorro-quente')
# E ao darmos o comando:
#    print(lanche)
# A saída seria:
#    ['cachorro-quente', 'hamburguer', 'suco', 'picole', 'cookie']
#
# ============================================ Usando o DEL ===========================================
# Podemos usar o comando:
#    del lanche[3]
# E ao darmos:
#    print(lanche)
# A saída seria:
#    ['cachorro-quente', 'hamburguer', 'suco', 'picole', 'cookie']
#
# ======================================== Usando o metodo POP() ======================================
# Podemos também usar o:
#    lanche.pop(3)
# E ao imprimirmos a Saída seria:
#    ['cachorro-quente', 'hamburguer', 'suco', 'picole', 'cookie']
# Se usarmos o pop sem darmos o argumento da indice ele irá remover o ultimo item:
#    lanche.pop()
# Saída:
#    ['cachorro-quente', 'hamburguer', 'suco', 'picole']
# ====================================== Usando o metodo REMOVE() =====================================
# Poderiamos usar inves do POP ou o DEL, o:
#    lanche.remove('pizza')
# E ao imprimirmos a Saída seria:
#    ['cachorro-quente', 'hamburguer', 'suco', 'picole', 'cookie']
#
# ======================================= Fazendo lista com o for =====================================
# Fazendo assim:
#    valores = list(range(4,11))
# A saída seria:
#    print(valores)
#    [4, 5, 6, 7, 8, 9, 10]
#
# Isso faria uma lista crescente, se quisessemos uma lista desorganizada poderiamos fazer:
#    valores = [8, 2, 5, 4, 9, 3, 0]
# A saída seria:
#    [8, 2, 5, 4, 9, 3, 0]
#
# ======================================= Usando o metodo sort() ======================================
# Poderíamos ordenar a lista usando o sort() sem problema nenhum:
#    valores.sort()
# A saída seria:
#    [0, 2, 3, 4, 5, 8, 9]
#
# E se quisermos fazer o contrario poderiamos usar o:
#    valores.sort(reverse=True)
# A saída seria:
#    [9, 8, 5, 4, 3, 2, 0]
# ============================================== Adendos ==============================================
# . Se usarmos um metodo para retirar um item da lista e não existir esse item dará o erro:
#    Erro: ValueError: list.remove(x): x not in list
# . Podemos evita esse erro usando o if:
#    if 'pizza' in lanche:
#         lanche.remove('pizza')
# . O operador in é muito útil em vário casos em que usamos listas
# . Podemos usar o len() para saber o tamanho da lista:
#    len(valores) # Resultado seria 7
# . O metodo INSERT() nao começa contando pelo 0
# ======================================== Fim da parte Teorica =======================================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Começo da parte Prática ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Metodo APPEND()
print('Metodo APPEND()')
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)

print()

# Metodo SORT()
print('Metodo SORT()')
num = [2, 5, 9, 1]
num.sort()
print(num)

print()

# Metodo SORT(REVERSE=True)
print('Metodo SORT(REVERSE=True)')
num = [2, 5, 9, 1]
num.sort(reverse=True)
print(num)

print()

# Metodo INSERT()
print('Metodo INSERT()')
num = [2, 5, 9, 1]
num.insert(2, 0)
num.insert(2, 2)
print(num)

print()

# Metodo POP sem indice
print('Metodo POP() sem indice')
num = [2, 5, 9, 1]
num.pop()

print()

# Metodo POP com indice
print('Metodo POP() com indice')
num = [2, 5, 9, 1]
num.pop(2)
print(num)

print()

# Metodo LEN()
print('Metodo LEN()')
num = [2, 5, 9, 1]
print(f'Essa lista tem {len(num)} elementos')

print()

# Metodo REMOVE() (usando o INSERT() para teste)
print('Metodo REMOVE()')
num = [2, 5, 9, 1]
num.insert(2, 2)
num.remove(2)  # Se tentarmos remover um numero que não está na lista dará um ValueError
print(num)

print()

# Complemetaçao do metodo REMOVE() usando o in
print('Complemetaçao do metodo REMOVE() usando o in')
num = [2, 5, 9, 1]
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4 na lista num')

print()

# Exemplo para criar uma lista bonita
print('Exemplo para criar uma lista bonita')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end='')

print('\n')

# Para achar o item e a indice usando o ENUMERATE() no for
print('Para achar o item e a indice usando o ENUMERATE() no for')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print()

# Ler numeros pelo teclado
# valores = list()
# print('Lendo numero pelo teclado')
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# print(valores)

print()

# Peculiaridade das Listas em Python
print('Peculiaridade das Lista em Python')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
