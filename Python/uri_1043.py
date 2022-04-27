x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
if(a < b + c) and (b < a + c) and (c < a + b):
  perimetro = a + b + c
  print('Perimetro = {:.1f}' .format(perimetro))
else:
  area = ((a + b) * c) / 2
  print('Area = {:.1f}' .format(area))