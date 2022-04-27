n = int(input())

h = int(n) / 3600
m = (int(n) - (int(h) *3600 )) / 60
s = int(n) - (int(h) * 3600) - (int(m) * 60)

tempo = str(int(h)) + ":" + str(int(m)) + ":" +  str(int(s))
print(tempo)