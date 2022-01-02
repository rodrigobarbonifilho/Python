from datetime import date as d
ano_atual = d.today().year
maiores = 0
menores = 0
for pess in range(1, 8):
    ano = input(f'Em que ano a {pess} pessoa nasceu? ')
    idade = ano_atual - int(ano)
    if len(ano) < 4 or len(ano) > 4:
        print('Ano Invalido')
        print()
    elif int(ano) > int(ano_atual):
        print('Ano Invalido!')
        print()
    elif idade >= 18:
        maiores += 1
    elif idade < 18:
        menores += 1
print()
print(f'Ao todo tivemos {maiores} pessoas maiores de idade!')
print(f'E tambem tivemos {menores} pessoas menores de idade!')
