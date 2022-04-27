c = input().split(" ")
a, b = c
a = int(a)
b = int(b)

if a == 1:
  tot = b * 4.00;

elif a == 2:
  tot = b * 4.50;

elif a == 3:
  tot = b * 5.00;

elif a == 4:
  tot = b * 2.00;

elif a == 5:
  tot = b * 1.50;
print("Total: R$ {:.2f}".format(tot))