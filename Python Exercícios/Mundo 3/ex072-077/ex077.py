palavras = ('Aprender',
            'Programar',
            'Linguagem',
            'Python',
            'Curso',
            'Gratis',
            'Estudar',
            'Praticar',
            'Trabalhar',
            'Mercado',
            'Programador',
            'Futuro',
            )

vogal = ''

# Meu Jeito
for item in palavras:
    print(f'\nNa palavra \033[31m{item: <11}\033[m temos as vogais: ', end='')
    for letra in range(0, len(item)):
        if item[letra] == 'A' or item[letra] == 'a':
            print('a', end=' ')
        elif item[letra] == 'E' or item[letra] == 'e':
            print('e', end=' ')
        elif item[letra] == 'I' or item[letra] == 'i':
            print('i', end=' ')
        elif item[letra] == 'O' or item[letra] == 'o':
            print('o', end=' ')
        elif item[letra] == 'U' or item[letra] == 'u':
            print('u', end=' ')

print()

# Jeito Guanabara
for item in palavras:
    print(f'\nNa palavra \033[31m{item: <11}\033[m temos as vogais: ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
