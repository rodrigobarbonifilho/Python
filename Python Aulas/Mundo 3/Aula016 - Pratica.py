lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Exibindo a tupla
print('Exibindo a tupla:')
print(lanche)
print()

# Fatiamento
print('Exemplos de fatiamento:')
print(lanche[1])
print(lanche[2])
print(lanche[-2])
print(lanche[1:3]) # Desconsidera-se o ultimo elemento
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print()

# Exemplos para ver a difereça
print('Vendo as diferenças:')
lanche1 = 'Hamburguer'
print(lanche)
print(lanche1)
print()

print('\033[1;31mOBS:Tuplas sao imutaveis!!!!\033[m')
# Tuplas sao imutaveis
# lanche[1] = 'Refrigerante'
# print(lanche)
print()

# Mostrando de jeito melhor
print('Vendo dentro de um for(estrutura de repetiçoes) como fica:')
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caramba')
print()

# Segunda maneira
for cont in range(len(lanche)):
    print(cont)

print()

for cont in range(len(lanche)):
    print(lanche[cont])

print()

# Terceira maneira
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {pos}')

print()

# ALGO QUE O GUANABARA FALOU
print(sorted(lanche))
print(lanche)

# Outra tuplas outros exemplos
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a)
print(b)
print(c)

print()

print(len(c))
print(c.count(5))
print(c.index(2, 4))

# Outra tupla
pessoa = ('Gustavo', 35, 'M', 99.88)
# del(pessoa[0])
print(pessoa)
