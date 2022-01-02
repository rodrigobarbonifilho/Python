print('-=' * 30)
 
# Fazer uma lista
valores = []

# Obter os valores e bota - los na lista na posição correta
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(valores):
        print('Adicionado ao final da lista...')
        valores.append(n)
    elif n < min(valores):
        print('Adicionado na posição 0...')
        valores.insert(0, n)
    else:
        pos = 0
        while pos <= len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)

# Mostrar a lista 
print(str(valores).replace('[', '').replace(']', ''))
print('-=' * 30)
