def mostrar(nome):
    try:
       a = open(nome, 'rt')
    except:
        print('erro ao ler')
    else:
        print('-' * len('pessoas cadastradas         '))
        print('    PESSOAS CADASTRADAS    ')
        print('-' * len('pessoas cadastradas         '))

        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')



def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Aconteceu um erro')
    else: 
        print('Arquivo criado')