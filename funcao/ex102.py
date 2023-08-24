

def fat(num, show):
    fatorial = 1
    
    while num != 0:
        if show:
            print(num, end='')
            if num > 1:
                print(' X ', end="")
            else:
                print(' = ', end="")  

        fatorial *= num     
        num -= 1

    return fatorial

    
    

print(fat(5, show=True))
