n1 = int (input ("1° Numero: "))
n2 = int (input ("2° Numero: "))
n3 = int (input ("3° Numero: "))
print("O menor é")
if ((n1<n2) & (n1<n3)) :
    print(n1)
elif((n2<n1) & (n2<n3)):
    print(n2)
elif((n3<n1) & (n3<n2)):
    print(n3)
print("O maior é")
if ((n1>n2) & (n1>n3)) :
    print(n1)
elif((n2>n1) & (n2>n3)):
    print(n2)
elif((n3>n1) & (n3>n2)):
    print(n3)