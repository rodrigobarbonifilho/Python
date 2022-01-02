# ======================================== Parte Teorica ========================================
# Listas Parte 2
# Vamos declarar uma lista:
#    dados = list()
# Que é uma variavel composta(que pode armazenar vários valores)
# Que podemos adicionar um item usando o comando:
#    dados.append('Pedro')
# Se eu der o comando:
#    print(dados[0])
# Saída:
#    ['Pedro']
# Ou ser eu der:
#    print(dados[1])
# 
# Vou declarar outra lista:
#    pessoas = list()
# E irei dar um append nela:
#    pessoas.append(dados[:])
# Criarei uma copia de dados e colocarei em pessoas:
# E a lista pessoas ficará assim:
#    pessoas:
#        'Pedro', 25   ,   Maria, 19  ,   'Joao', 32  # Dados da lista dados dentro da lista pessoas
#           0      1        0      1        0      1  # Indices dentro da lista
#              0               1               2  # Indices da lista pessoas
# E para eu criar essa lista de uma forma diferente:
#    pessoa = [['Pedro', 25], ['Maria', 19], ['João', 32]]
# E estas são chamadas de lista compostas
# Se eu der:
#    print(pessoas[0][0]) # Significa que eu estou chamando o indice 0 da lista pessoas e dentro desse indice
#                           temos outra lista que eu estarei chamando o indice 0 dessa lista
# Saída:
#    'Pedro'
# Outros exemplos:
#   print(pessoas[1][1])
#   print(pessoas[2][0])
# Saída:
#   19
#   'João'
#
# E se eu der:
#   print(pessoas[1])
# A saída será:
#   ['Maria', 19]
# ========================================== Parte Prática ========================================
print('-=' * 30)
# Criando um exemplo normal:
print('Criando um exemplo normal:')
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

print()

# Botando uma lista dentro de outra lista:
print('Botando uma lista dentro de outra lista:')
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

print()

# Fazendo um teste:
print('Fazendo um teste:')
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print()
# Declarando de outra forma:
print('Declarando de outra forma:')
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print('Mandando imprimir galera:')
print(galera)

print()

# Se eu der: print(galera[0]) a saída será:
print('Se eu der: print(galera[0]) a saída será:')
print(galera[0])

print()

# Imprimindo galera[0][1]:
print('Imprimindo galera[0][1]:')
print(galera[0][1])

print()

# E se eu mandar imprimir galera[2][1]:
print('E se eu mandar imprimir galera[2][1]: ')
print(galera[2][1])

print()

# Eu posso tambem fazer o seguinte:
print('Eu posso tambem fazer o seguinte:')
for p in galera:
    print(p)

print()

# Se eu quiser só os nomes:
print('Se eu quiser só os nomes:')
for p in galera:
    print(p[0])

print()

# Se eu quisesse só a idade:
print('Se eu quisesse só a idade:')
for p in galera:
    print(p[1])

print()

# Para deixar mais bonito:
print('Para deixar mais bonito:')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print()

# Posso fazer tambem isso:
# galera = []
# dados = []
# print('Posso fazer tambem isso:')
# for c in range(0, 3):
#     dados.append(input('Nome: '))
#     dados.append(int(input('Idade: ')))
#     galera.append(dados[:])  # Muito importante essa cópia da lista dados
#     dados.clear()
# print(galera)

# print()

# Poderia mostrar tambem só as pessoas com mais de 20 anos:
# print('Poderia mostrar tambem só as pessoas com mais de 20 anos:')
# totmai = totmen = 0
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade.')
#        totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totmen += 1

# print(f'Temos {totmai} maiores e {totmen} menores de idade')
print('-=' * 30)
