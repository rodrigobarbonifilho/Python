
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda  nota: '))
media = (n1 + n2) / 2
if n1 or n2 > 10:
    print('Nota Invalida! A nota maxima é 10!')
elif media < 5:
    print('Tirando {:.2f} e  {:.2f}, a média do aluno é: {:.1f}'.format(n1, n2, media))
    print('\033[1;31mO aluno está REPROVADO\033[m')
elif 5 < media <= 6.9:
    print('Tirando {:.2f} e  {:.2f}, a média do aluno é: {:.1f}'.format(n1, n2, media))
    print('\033[1;33mO aluno está de RECUPERÇÃO\033[m')
elif media >= 7:
    print('Tirando {:.2f} e  {:.2f}, a média do aluno é: {:.1f}'.format(n1, n2, media))
    print('\033[1;32mO aluno está APROVADO!\033[m')
