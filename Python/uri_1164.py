testes = int(input())

for i in range(testes):
    n = int(input())

    valor = 1
    soma = 0

    while valor < n:
        if n % valor == 0:
            soma = soma + valor

        valor = valor + 1

    if soma == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')