"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

# Criar as listas
valores = []
ímpares = []
pares = []
print('-=' * 30)

# Ler os números
resp = True
while resp:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N]: ')
    if resp in 'Nn':
        resp = False

# Adicionar numeros pares na lista 'pares' e ímapares na lista 'ímpares'
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)

# Mostrar as listas
print('-=' * 30)
print(f'A lista completa é: {str(valores).replace("[", "").replace("]", "")}')
print(f'A lista de pares é: {str(pares).replace("[", "").replace("]", "")}')
print(f'A lista de ímpares é: {str(ímpares).replace("[", "").replace("]", "")}')
print('-=' * 30)
