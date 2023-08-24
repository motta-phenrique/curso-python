def leiaint(msg):
    ok = False
    valor = 0
    while True:
        try:
            valor = int(input(msg))
        except(ValueError, TypeError):
            print('Erro no tipo de dados digitado')
        except Exception as erro:
            print(f'Erro encontrado foi: {erro.__cause__}')
        else:
            ok = True
            if ok:
                break
    
    return valor


def leiafloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            valor = float(input(msg))
        except(ValueError, TypeError):
            print('Erro no tipo de dados digitado')
        except Exception as erro:
            print(f'Erro encontrado foi: {erro.__cause__}')
        else:
            ok = True
            if ok:
                break
    
    return valor


num = leiaint('Digite um numero inteiro: ')

num2 = leiafloat('Digite um numero real: ')
print(f'o numero inteiro é {num}, e o real é {num2}')