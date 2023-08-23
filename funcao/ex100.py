from random import randrange

def sorteia(lista):
    for i in range(0, 5):
        n = randrange(0, 11)
        lista.append(n)

    print(lista)


def somaPar(lista):
    s = 0
    for i, n in enumerate(lista):
        if lista[i] % 2 == 0:
            s += lista[i]
    
    print(s)



lista = list()

sorteia(lista)
somaPar(lista)