print(f'{" LOJAS BARBONI ":=^40}')
# noinspection NonAsciiCharacters
preço = float(input('\033[1;mPreço das compras: R$ \033[m'))
print("""FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
escolha = input('Qual sua opção? ')

print()

if escolha == '1':
    total = preço - (preço * 10 / 100)
elif escolha == '2':
    total = preço - (preço * 5 / 100)
elif escolha == '3':
    total = preço
    parcelas = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas} SEM JUROS')
elif escolha == '4':
    parcelas = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    valor_das_parcelas = total / parcelas
    print(f'Voce pagara em {parcelas}x de R${valor_das_parcelas} COM JUROS')
else:
    total = '0'
    print('\033[1;31mEscolha Invalida!\033[m')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final!')
print(f'{" LOJAS BARBONI ":=^40}')
