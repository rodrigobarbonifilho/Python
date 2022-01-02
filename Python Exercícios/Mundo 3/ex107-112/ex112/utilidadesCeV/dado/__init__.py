def leiaDinheiro(msg):
    """
    -> Função para validar um preço float
    :param msg: Mensagem a ser exibida
    :return: retorna um valor float
    """
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
