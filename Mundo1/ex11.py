l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
latas = (l*h)/2
print('A área é igual à {}m2, são necessárias {:.0f} latas de tintas para pintar as paredes'.format(l*h, latas))
