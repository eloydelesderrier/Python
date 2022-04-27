x = int(input())
z = int(input())

cont = 0
i = 1

while z<=x:
    z = int(input())

cont = x
i = 1
auxiliar = cont
s = 0
while auxiliar < z:
    cont = cont + i
    auxiliar = cont + auxiliar
    s +=1
print(s+1)