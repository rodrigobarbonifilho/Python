# Criando a lista
matriz = [[], [], []]
print('-=' * 30)

# Recebendo e colocando os valores nas listas
for i in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para a posição [0, {i}]: ')))
for i in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para a posição [1, {i}]: '))) 
for i in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para a posição [2, {i}]: ')))
print()

print('-=' * 30)

# Mostrar a matriz formatada
for n in matriz[0]:
    print(f'[{n:^5}]', end=' ')
print()
for n in matriz[1]:
    print(f'[{n:^5}]', end=' ')
print()
for n in matriz[2]:
    print(f'[{n:^5}]', end=' ')
print()

print('-=' * 30)
# 2° Jeito
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para a posição [{l}, {n}]: ')))
print('-=' * 30)
for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}] ', end='')
    print()
