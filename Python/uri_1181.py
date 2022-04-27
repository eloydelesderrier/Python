L = int(input())
T = input()

tamanho = 12
matriz = []

for i in range(tamanho):
    linha = []
    for i in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)
    
if T == 'S':
    soma = 0
    for v in matriz[L]:
        soma = soma + v
    print(soma)

elif T == 'M':
    media = 0
    soma = 0
    for v in matriz[L]:
       soma = soma + v
       media = soma / tamanho
    print(media)