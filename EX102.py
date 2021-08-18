def fatorial(n,show):
    fat=1
    for a in range (1,n+1):
        if show==True:
            print(f'{a} X ',end='')
        fat*=a

    return fat

print('=',fatorial(5,True))