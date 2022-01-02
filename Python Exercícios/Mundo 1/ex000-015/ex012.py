# coding=utf-8
"""preço = float(input('Coloque aqui o preço do produto:R$'))
desconto = preço * 5 / 100 
desconto2 = preço - desconto
print('O produto que custava R${},agora com o desconto de 5% custa R${}'.format(preço, desconto2))"""
# Tentar de outro jeito

preço = float(input('Coloque aqui o valor do produto:R$'))
porcentagem = int(input('Coloque aqui o desconto:%'))

desconto = porcentagem * preço / 100
desconto2 = preço - desconto

print()

print('\033[1;33mO produto que custava R${:.2f},agora com o desconto de %{},custa R${:.2f}\033[m'.format(preço, porcentagem, desconto2))
