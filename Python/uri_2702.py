entrada1 = input()
linha1 = entrada1.split()
frango = int(linha1[0])
bife = int(linha1[1])
massa = int(linha1[2])
entrada2 = input()
linha2 = entrada2.split()
Pfrango = int(linha2[0])
Pbife = int(linha2[1])
Pmassa = int(linha2[2])
SS = 0

if Pfrango - frango > 0:
  SS += Pfrango - frango
if Pbife - bife > 0:
  SS += Pbife - bife
if Pmassa - massa > 0:
  SS += Pmassa - massa
print(SS)