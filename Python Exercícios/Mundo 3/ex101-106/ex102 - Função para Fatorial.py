def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    print('_' * 30)
    if show == False:
        for c in range(n, 1, -1):
            f *= c
        return f
    else:
        for c in range(n, 1, -1):
            f *= c
            if n == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        return f
        print()


# Programa principal
print(fatorial(6))
print(fatorial(5, show=False))
print(fatorial(5, show=True))
help(fatorial)
