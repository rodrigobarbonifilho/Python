# coding=utf-8
temperatura = float(input('\033[4;33mColoque aqui uma tenperatura em °C:\033[m'))

Fahrenheit = temperatura * 1.8 + 32

print('\033[1;31mConvertendo {}°C para Fahrenheit vai ter {}°F\033[m'.format(temperatura, Fahrenheit))
