def leiaInt(msg):
    """
    → É um input que só aceita tipo Int
    :param msg: Mensagem a ser exibida
    :return: retorna o número digitado pelo úsuario
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor, digite um valor inteiro válido\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    """
    → É um input que só aceita tipo Float
    :param msg: Mensagem a ser exibida
    :return: O número digitado pelo úsuario
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor, digite um valor real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO úsuario preferiu não informar esse número!')
            return 0
        else:
            return n
