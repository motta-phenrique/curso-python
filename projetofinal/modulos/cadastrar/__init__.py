def cadastrar(arq):
    print('-' * len('TELA DE CADASTRO         '))
    print('    TELA DE CADASTRO    ')
    print('-' * len('TELA DE CADASTRO         '))

    nome = input('Nome: ')
    idade = int(input('Idade: '))

    try: 
        a = open(arq, 'at')
    except:
        print('erro na abertura')
    else:
        try:
            a.write(f'{nome};{idade} \n')
        except:
            print('houve um erro, na hora de escrever')
        else:
            print(f'novo registro: {nome} adicionado')
            a.close()