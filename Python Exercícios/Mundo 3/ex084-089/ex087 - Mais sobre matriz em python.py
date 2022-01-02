# Definindo variaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valores = [[0], [0], [0]]
sp = s3c = m2c = 0

print('-=' * 30)

# Vendo a matriz
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l][n] = int(input(f'Digite um valor para a posição [{l}, {n}]: '))

# Vendo qual é a soma dos valores pares digitados nessa matriz:
        if matriz[l][n] % 2 == 0:
            sp += matriz[l][n]

# Vendo qual é a soma de todas os valores da terceira coluna:
        if n == 2:
            s3c += matriz[l][n]
        
# Vendo qual é o maior número na segunda coluna:
        if l == 1:
            if m2c == 0 or matriz[l][n]:
                m2c = matriz[l][n]
            
# Atribuindo valores a variaveis
valores[0], valores[1] = sp, s3c

print('-=' * 30)

for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}] ', end='')
    print()

print('-=' * 30)

# Mostrando a soma de todos os valores pares digitados.                                                                  
print(f'A soma de todos os números pares é de: {valores[0]}')

# Mostrando a soma dos valores da terceira coluna.
print(f'A soma de todos os números da 3° coluna é de: {valores[1]}')

# Mostrando o maior valor da segunda linha.
print(f'O maior valor da segunda linha é o número: {m2c}')
