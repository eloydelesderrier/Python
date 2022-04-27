valor = float(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print('NOTAS:')
for nota in notas:
    qtd_nota = int(valor / nota)
    print('{} notas(s) de R$ {:.2f}'.format(qtd_nota, nota))
    valor -= qtd_nota * nota