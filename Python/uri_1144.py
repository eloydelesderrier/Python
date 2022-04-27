y = 0
x = int(input())
n = 1

while (y < x):
  print("%d %d %d" %(n, n**2, n**3))
  print("%d %d %d" %(n, n**2+1, n**3+1))
  n += 1
  y+= 1