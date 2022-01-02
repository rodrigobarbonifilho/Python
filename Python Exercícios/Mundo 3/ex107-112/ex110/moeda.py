def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Esa função retorna o valor passado mais um aumento
    :param preco: Valor a ser passado
    :param taxa: Quanto será o aumento
    :param formato: (parâmetro opcional) Definirá se o retorno será formatado ou não
    :return: Retorna o preco mais a taxa
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Essa função retorma o valor passado menos um desconto
    :param preco: Valor a ser passado
    :param taxa: Quanto será o desconto
    :param formato: (parâmetro opcional) Definirá se o retorno será formatado ou não
    :return: Retorna o valor menos a taxa
    """
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Essa função retorna o dobro do valor passado
    :param preco: É o valor a ser passado
    :param formato: (parâmetro opcional) Definirá se o retorno será formatado ou não
    :return: Retorna o preco * 2
    """
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    """
    -> Essa função retorna a metade do valor passado
    :param preco: É o valor a ser passado
    :param formato: (parâmetro opcional) Definirá se o retorno será formatado ou não
    :return: Retorna a metade do preco
    """
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0.00, valor_da_moeda='R$'):
    """
    -> Essa função formata o valor passado para um valor monetário válido
    :param preco: É o valor a ser formatado
    :param valor_da_moeda: É para qual é a moeda a ser formatada
    :return: Uma f-string em valor monetário
    """
    return f'{valor_da_moeda} {preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa_a=0, taxa_d=0):
    """
    -> Vai retornar um resumo de todas as funções já feitas
    :param preco: Valor a ser passado
    :param taxa_a: Aumento
    :param taxa_d: Desconto
    :return: Retorna uma tabela com os resultados
    """
    print('-' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('-' * 30)
    print('\033[m', end='')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preco, taxa_a, True)}')
    print(f'{taxa_d}% de redução: \t{diminuir(preco, taxa_d, True)}')
    print('-' * 30)






