# Funções:
def notas(*n, sit=False):
    """
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    -> Função para avaliar notas e situações de vários alunos.
    :param n: Uma ou mais notas de alunos (aceita vários).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """
    # Váriaveis Locais
    dici = {}
    c = maior = menor = media = 0

    for num in n:    
    # A maior e menor nota
        if c == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    
    # A quantidade de notas informadas
        c += 1

    # Média das notas
        media += num
    media /= c

    dici['total'] = c
    dici['maior'] = maior
    dici['menor'] = menor
    dici['média'] = media

    # Situações:
    # RUIM
    if sit:
        if media < 5:
            situação = 'RUIM'
    # RAZOÁVEL
        elif media < 7:
            situação = 'RAZOÁVEL'
    # BOA
        else:
            situação = 'BOA'
        dici['situação'] = situação
    return dici    


# Programa principal:
resp = notas(1, 5, 7, 10, 2, sit=True)
for k, v in resp.items():
    print(f'O campo {k} tem o valor {v}.')
print(resp)

print()

help(notas)
