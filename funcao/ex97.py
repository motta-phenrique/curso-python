from time import sleep

def contador(inicio, fim, passo):
    
    if inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(i, end=" ")
            
    else:
        for i in range(inicio, fim+1, passo):
            print(i, end=" ")
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez agora')
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o intervalo: '))

contador(i, f, p)