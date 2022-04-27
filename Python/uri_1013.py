entry = input().split()
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])

maior = (a + b + abs(a - b)) / 2
valor = (maior + c + abs(maior - c)) / 2
print('%d eh o maior' %valor)