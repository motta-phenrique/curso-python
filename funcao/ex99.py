def maior(*num):
    maior = 0

    for i, n in enumerate(num):
        if num[i] > maior:
            maior = num[i]
    
    print(f'Foram analisados {len(num)} numeros e o maior é {maior}')


maior(1, 4, 0, 7, 9)
maior(0, 2)