def maior(*num):
    mai=0
    for i in num:
        if len(num)==1:
            mai=num
        else:
            if i >mai:
                mai=i
    print(f'O maior numero é: {mai}')

maior(2 ,1 ,10 ,8 ,100 ,3 )
