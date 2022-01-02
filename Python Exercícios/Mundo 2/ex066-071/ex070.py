print(f'{" INICIO DO PROGRAMA ":=^40}')
print(40*'-')
print(f'{" Lojas Super Baratão ": ^40}')
print(40*'-')
tot, pm1000, npmb, pmb = 0, 0, '', 0
while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço do produto: '))
    if pmb == 0 or preco < pmb:
        pmb, npmb = preco, produto
    if preco >= 1000:
        pm1000 += 1
    resposta = input('Voce quer continuar? [S/N]: ').upper().strip()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = input('Voce quer continuar/ [S/N]: ').upper().strip()[0]
    tot += preco
    if resposta == 'N':
        break
print(f'{" FINAL DO PROGRAMA ":=^40}')
print(f'O valor total é de: R${tot:.2f}')
print(f'Foi informado {pm1000} produto(s) com mais de R$1000,00.')
print(f'O produto mais barato foi o(a) {npmb} que custou R${pmb:.2f}')
