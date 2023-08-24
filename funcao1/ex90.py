aluno = dict()

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Media do aluno: '))

print(f'nome = {aluno["nome"]}')
print(f'media = {aluno["media"]}')

if aluno['media'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')