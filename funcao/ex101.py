def voto(ano):
    idade = 2023 - ano_nas

    if idade >= 65:
        print(f'com {idade} anos o voto é opcional.')
    elif idade >= 18:
        print(f'Com {idade} anos o voto é obrigatório')
    else:
        print(f'com {idade} anos não vota!')




ano_nas = int(input('Digite o ano que voce nasceu: '))

voto(ano_nas)