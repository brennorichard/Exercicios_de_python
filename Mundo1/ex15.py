dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram percorridos? '))
valor = dias*60 + km*0.15
print('O valor total a ser pago é de R${}'.format(valor))
