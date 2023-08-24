def fat(num):
    fatorial = 1
    
    while num != 0:
        fatorial *= num     
        num -= 1

    return fatorial