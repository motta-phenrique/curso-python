def fat(num):#Função com parametro e retorno
    fatorial = 1
    
    while num != 0:
        fatorial *= num     
        num -= 1

    return fatorial


print(fat(5))


def mostra_msg():# função sem parametro e sem retorno
    print('Olá mundo')


mostra_msg()


def soma(n2, n3): # Com parametro e sem retorno
    print(n2 + n3)


soma(1, 3)