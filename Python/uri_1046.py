x = input().split()
ti = int(x[0])
tf = int(x[1])
if(ti == tf):
  print('O JOGO DUROU 24 HORA(S)')
else:
  tt = tf - ti
  if(tt < 0):
    tt += 24
  print('O JOGO DUROU %d HORA(S)' %tt)