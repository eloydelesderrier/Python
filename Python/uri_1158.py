n = int(input())

for i in range(n):
    valor = input().split()
    x = int(valor[0])
    y = int(valor[1])

    if x % 2== 0:
        x+=1

    soma = 0
    for k in range(y):
        soma +=x
        x+=2
    print(soma)