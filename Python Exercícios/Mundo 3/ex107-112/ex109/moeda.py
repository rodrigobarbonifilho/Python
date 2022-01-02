def moeda(preco=0.00, valor_da_moeda='R$'):
    """
    -> Essa função formata o valor passado para um valor monetário válido
    :param preco: É o valor a ser formatado
    :param valor_da_moeda: É para qual é a moeda a ser formatada
    :return: Uma f-string em valor monetário
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def metade(preco=0, formato=False):
    """
    -> Essa função retorna a metade do valor passado
    :param preco: É o valor a ser passado
    :param formato: (parâmetro opcional) Definirá se o retorno será formatado ou não
    :return: Retorna a metade do preco
    """
    res = preco / 2
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
