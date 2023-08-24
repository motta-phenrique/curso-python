import moedas

p = int(input('digite o preço: '))
au = float(input('Valor que deseja aumentar: '))
dim = float(input('Valor que deseja diminuir: '))

print(f'A metade do valor é {moedas.metade(p)}')
print(f'o dobro do valor é {moedas.dobro(p)}')
print(f'Aumentando {au}% temos {moedas.aumento(p, au)}')
print(f'Diminuindo {dim}% temos R${moedas.reduz(p, dim)}')
