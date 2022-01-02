# Criar uma lista para guardar os valores
valores = list()
cont = maior = menor = 0

# Receber pelo teclado esse valores
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {p}: ')))
print(30*'-=')

# Definir qual é o maior e o menor e nas suas respectivas posições
for v in valores:
    if cont == 0:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    cont += 1

# Mostrar os resultados
print(f'Você digitou os valores: {str(valores).replace("[", "").replace("]", "")}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')

for v, i in enumerate(valores):
    if i == maior:
        print(v, end='... ')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')

for v, i in enumerate(valores):
    if i == menor:
        print(v, end='... ')
