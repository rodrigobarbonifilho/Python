from colorama import init
init()
cores = {
    'branco': '\033[m',
    'vermelho': '\033[1;31m'
}


#Funções
def leiaInt(msg):
    """
    -> ReceBe um número e verifica se esse número é do tipo inteiro
    :param msg: A mensagem que será mostrada
    """
    n = input(msg)
    while not n.isnumeric():
        print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido!{cores["branco"]}')
        n = input(msg)
    return n


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
