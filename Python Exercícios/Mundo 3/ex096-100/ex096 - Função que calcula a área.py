def calcula_area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}m².')


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
larg = float(input('LARGURA [m]: '))
comp = float(input('COMPRIMENTO [m]: '))
calcula_area(larg, comp)
