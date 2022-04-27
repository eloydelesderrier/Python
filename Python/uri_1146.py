x = 1
y = []

while x != 0:
    x = int(input())
    for i in range(1, x+1):
        y.append(i)
        y[i-1] = str(y[i-1])
        i +=i
        
    y=' '.join(y)
    if x!=0:
        print(y)
        y=[]