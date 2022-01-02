# Variaveis de contador

cont = 0
homemV = ''
idadeHoV = 0
mulheresMN20 = -0
media = 0
# Analisador completo

for p in range(1, 5):
    print(f'------ {p}ª PESSOA ------')
    # Nome
    nome = input('Nome: ').strip()

    # Idade
    idade = int(input('Idade: '))

    # Sexo
    sexo = input('Sexo[M/F]: ').upper().strip()

    # Definindo a media do grupo
    media += idade
    if p == 4:
        media = media / 4

    # Achar o homem mais velho
    if p == 1 and sexo == 'M':
        homemV = nome
        idadeHoV = idade
    else:
        if idade > idadeHoV and sexo == 'M':
            homemV = nome
            idadeHoV = idade

    # Achar quantas mulheres tem menos de 20 anos
    if sexo == 'F':
        if idade <= 20:
            mulheresMN20 += 1

# Mostrando as informaçoes pedidas no enunciado
print(23*'-')
print()
print(f'A media de idade do grupo é de: {media:.1f} anos')
if idadeHoV == 0 or homemV == '':
    print('Nao foi informado nenhum homem!')
else:
    print(f'O homem mais velho do grupo tem {idadeHoV} anos e se chama {homemV}')
if mulheresMN20 == 0:
    print('Nao foi informada nenhuma mulher com menos de 20 anos!')
else:
    print(f'Ao todo sao {mulheresMN20} mulheres com menos de 20 anos')
