# Tratamento de Erros e Exceções Aula 023 - Parte Prática e Teórica
# E isto é para "ERROS" não:
#    primt(x)
# Isto é um erro de sintaxe pois o certo é:
#    print(x)
# Que é um erro síntatico, mas esse código acima tem um erro:
esc = input('Você quer ver a parte teórica ou pratica: ')
if esc.upper() in 'TEÓRICATEORICA':
    print('-=' * 30)
    print('Parte Teórica → Exemplo 1'.center(60))
    print('-=' * 30)
    print('Vamos ver o exemplo de parte Teórica:')
    print('Se eu printar "Oi" → ', end='')
    print('Oi')
    print('Agora se eu printar "x"  → ', end='')
    print('NameError: name "x" is not defined')
    print('-=' * 30)
# O erro se dá pois a váriavel x não existe
# e quando o comando é um que normalmente funcionaria mas deu um erro
# chamamos isso de exceção:
    print('Parte Teórica → Exemplo 2'.center(60))
    print('-=' * 30)
    n = int(input('Número: '))
    print(f'Você digitou o número → {n}')
    print('Ele acaba recebendo o erro → ValueError: invalid literal for int() with base 10: "oito"')
    print('-=' * 30)
# Vamos para mais um exemplo:
#    r = a / b
    print('Parte Teórica → Exemplo 3'.center(60))
    print('-=' * 30)
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
    print(f'O resultado → {r}')
    print('Se eu tentar dividir por zero → ZeroDivisionError: division by zero')
    print('-=' * 30)
# Vamos de outro exemplo:
#    r = 2 / '2'
# É uma exceção de TypeError pois o Python não considera um número entre aspas
# Outro exemplo:
#   lst = [3, 6, 4]
#   print(lst[3])
# Dará um erro IndexError no caso do Dicionário é KeyError
# Vamos dar de exemplo o Módulo:
#    import uteis
# E o Python não encontre esse módulo dará um erro de ModuleNotFoundError
# E alguns dos erros possiveis são:
#    NameError
#    ValueError
#    ZeroDivisionError
#    TypeError
#    IndexError
#    KeyError
#    EOFError
#    KeyBoardInterruput
#    OSError
#    MemoryError
#    ConnectionError
#    RuntimeError
# Toda exceção vem de uma subclasse chamada Exception (Exceção em Portugueissssss)
# Vamos usar o try:
# try:
#    pass
# except:
#    pass
elif esc.upper() in 'PRÁTICAPRATICA':
    print('-=' * 30)
    print('Parte Pratica'.center(60))
    print('-=' * 30)
    print(' 1° Exemplo usando o Try and Except '.center(60))
    print('-=' * 30)
    # Isto é um Tratamento de Erro
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    # Podemos usar o mais execepts e com uma variavel de controle ± como no for
    except (TypeError, ValueError):
        print('Tivemos um problema com os tipos de dados que você digitou.')
    except ZeroDivisionError:
        print('Não é possivel dividir um número por zero!')
    except KeyboardInterrupt:
        print('O úsuario preferiu não informar os valores!')
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__cause__}')
    # O else e o finally são opcionais
    else:
        print(f'O resultado é {r:.2f}')
    finally:
        print('Volte Sempre Muito Obrigado!')
    print('-=' * 30)
else:
    print(f'Não encontramos nenhuma parte denominada {esc}')
