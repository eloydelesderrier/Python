testes = int(input())

for i in range(testes):
    n = int(input())
    cont = 0 
    for k in range(1, n+1):
        if n % k == 0:
            cont = cont + 1
           
            
    if cont != 2:
        print(f'{n} nao eh primo')
    elif cont == 2:
        print(f'{n} eh primo')