teste = int(input())
n = list(map(int, input().split()))
vetor = list
posicao = cont = 0
menor = n

for i in n:
    if i < n:
        menor = i
        posicao = cont
    cont+=1
print(f'Menor valor: {menor}')
print(f'posicao: {posicao}')