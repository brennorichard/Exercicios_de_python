valor = float(input('Qual o valor do produto que receberá desconto? '))
desconto = valor*0.05
print('O produto que custava R${}, custurá R${:.2f} com 5% de desconto'.format(valor, valor-desconto))
