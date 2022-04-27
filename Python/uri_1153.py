def fatorial(n):
    fat = [x for x in range(1, n+1)]
    return fat

n = 1
for i in (fatorial(int(input()))):
    n *= i
print(n)