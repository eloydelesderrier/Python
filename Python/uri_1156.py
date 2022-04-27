x = 1
s = 0

for i in range(1, 40, 2):
    m = i/x
    s = s + m
    x = x * 2
print("{:.2f}".format(s))