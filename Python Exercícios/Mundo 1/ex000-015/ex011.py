# coding=utf-8
lar = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
mq = lar * alt
tinta = mq / 2
print('\033[1;36mUma parede com {}X{} com sua area de {}m² '
      '\nPrecisará de {}L de tinta, para ser pintada\033[m.'.format(lar, alt, mq, tinta))
