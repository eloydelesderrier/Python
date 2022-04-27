x = list(map(int, input().split()))
y = 1
k = 0

while x[y] <=0:
    if x[y] <=0:
        y+=1
    if x[y]>0:
        break

for i in range(0,x[y]):
    k = k + x[0] + i
print(k)