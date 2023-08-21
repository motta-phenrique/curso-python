import time

pessoa = dict()

pessoa['nome'] = input('digite seu nome: ')
datanasc = int(input('digite o ano que voce nasceu: '))
data = time.localtime()
ano_atual = data.tm_year
pessoa['idade'] =ano_atual - datanasc
pessoa['ct'] = int(input('Digite o numero da sua carteira de trabalho (0 igual não tem): '))

if pessoa['ct'] != 0:
    pessoa['ano_cont'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite seu salario: '))
else:
    for k, i in pessoa.items():
        print(f'{k} = {i}')

aposentadoria = pessoa['ano_cont'] + 35
idade_aposentadoria = aposentadoria - datanasc

pessoa['aposentadoria'] = idade_aposentadoria

for k, i in pessoa.items():
    print(f'{k} = {i}')