# Jeito que achei de resolver
lista = []
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    lista.append(peso)
print(f'O maior peso lido foi: {max(lista):.1f}Kg')
print(f'O menor peso lido foi: {min(lista):.1f}Kg')
print()

# Jeito que entendi do video
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi: {maior:.1f}Kg')
print(f'O menor peso lido foi: {menor:.1f}Kg')
