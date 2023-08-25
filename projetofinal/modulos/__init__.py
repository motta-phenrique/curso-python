import verpessoas, cadastrar

arq = 'pessoas.txt'

if not verpessoas.arqExiste(arq):
    verpessoas.criarArquivo(arq)

while True:

    print('-' * len('menu principal         '))
    print('    MENU PRINCIPAL    ')
    print('-' * len('menu principal         '))

    print('1 - VER PESSOAS CADASTRADAS')
    print('2 - CADASTRAR NOVAS PESSOAS')
    print('3 - SAIR DO SISTEMA')

    n = int(input('Sua escolha: '))

    if n == 1:
        verpessoas.mostrar(arq)
    elif n == 2:
        cadastrar.cadastrar(arq)
    elif n == 3:
        break
    else:
        print('Voce digitou errado, digite um valor valido')