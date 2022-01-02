# coding=utf-8
from time import sleep

velocidade_carro = int(input("Qual a velocidade atual do carro? "))
multa = float((velocidade_carro - 80) * 7)

sleep(0.30)

if velocidade_carro > 80:
    print('\033[4;31mMULTADO!Voce excedeu o limite permitido que é de 80Km/h')
    print('voce deve pagar uma multa de R${:.2f}.\033[m'.format(multa))
print('\033[1;33mTenha um bom dia! Dirija com segurança!\033[m')
