# Defini uma listagem com os itens que serao mostrados
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)

# Enfeintando o codigo
print(20*'--')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(20*'--')

# Mostrar a listagem em uma ordem

item, preco, indice = 0, 1, 0
while indice < 17:
    print(listagem[item], end='')
    # Deixando bonito a listagem

    letras = len(listagem[item])
    pnts = 30 - letras
    print(pnts*'.', end='')
    # Deixando bonito a listagem

    print(f'R$ {listagem[preco]: >6.2f}')
    indice += 2
    item += 2
    preco += 2
print(20*'--')

print()

# Jeito que o Guanabara fez com 19 linhas '-'
print(40*'-')
print(f'{"LISTAGEM DE PREÇO":^40}')
print(40*'-')
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7}')
print(40*'-')
