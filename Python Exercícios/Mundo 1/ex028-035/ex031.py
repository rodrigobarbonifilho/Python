# coding=utf-8
# Jeito de estrutura condicional composta
distancia = float(input('Qual é a distancia da sua viagem? '))  # Distancia da viagem

print('\033[1;32mVoce esta prestes a começar uma viagem de {:.2f}.\033[m'.format(distancia))
if distancia <= 200.00:
    custo = distancia * 0.50  # Preço da viagem de menos de 200Km
else:
    custo = distancia * 0.45  # Preço da viagem acima de 200Km
print('E o preço da sua passagem será de R${:.2f}.'.format(custo))

print()

# jeito de estrura condicional simples
distancia = float(input('Qual é a distancia da sua viagem? '))  # Distancia da viagem

print('Voce esta prestes a começar uma viagem de {:.2f}.'.format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('E o preço da sua passagem será de R${:.2f}.'.format(preco))
