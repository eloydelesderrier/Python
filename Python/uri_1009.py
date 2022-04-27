nome = input()
sal_fixo = float(input())
qtd_vendas = float(input())

bonus = float(qtd_vendas * (15/100))

total = sal_fixo + bonus

print("TOTAL = R$ {:.2f}" .format(total)) 