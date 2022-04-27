x = int(input())
cont = 0

if x<=10000:
  while cont<x:
    y, z = map(int, input().split())
    if y>0 and z>0:
      soma = y+z
      print(soma)
    cont+=1  