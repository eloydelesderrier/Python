C = int(input())
T = input()

matriz = []
tamanho = 12

for i in range(tamanho):
    linha= []
    for k in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

coluna = []
for c in range(tamanho):
    coluna.append(matriz[c][C])

result = 0

if T == 'S':
    result = sum(coluna)

elif T == 'M':
    result = sum(coluna) / len(coluna)

print('{:.1f}'.format(result))