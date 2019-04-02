def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
        
vstup = int(input('Kolik opakovani?'))
prvniCislo = 0
druheCislo = 1
count = 0





if vstup <= 0:
    print('Musi to byt pozitivni.')
elif vstup == 1:
    print('Fibonacciho posloupnost je:', vstup, ':')
    print(prvniCislo)
else:
    print("Fibonacci sequence up to", vstup, ':')
    while count < vstup:
        print(prvniCislo)
        noveCislo = prvniCislo + druheCislo
        prvniCislo = druheCislo
        druheCislo = noveCislo
        count += 1

