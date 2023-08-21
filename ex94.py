pessoas = dict()
grupo = list()
mulheres = list()
acima = list()
total = 0
media = 0
while True:
    pessoas['nome'] = input('Digite o nome: ')
    pessoas['sexo'] = input('Sexo: F/M ').upper()
    pessoas['idade'] = int(input('Idade: '))

    media += pessoas['idade']
    
    total += 1

    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas.copy())

    if pessoas['idade'] > 22:
        acima.append(pessoas.copy())

    grupo.append(pessoas.copy())
    escolha = input('Quer continuar? S ou N ').upper()

    if escolha == 'N':
        break
 
media = media / total

print(f'total de pessoas: {total}')
print(f'media: {media:.2f}')
print(f'lista das mulheres: {mulheres}')
print(f'Pessoas acima da media: {acima} ')