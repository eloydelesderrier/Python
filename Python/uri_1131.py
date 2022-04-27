v = 1 
v_gremio = 0
v_inter = 0
empate =0 
grenais=0
while v == 1:
    gols = input().split(" ")
    inter = int(gols[0])
    gremio = int(gols[1])
    
    if inter > gremio:
        v_inter+=1
    elif gremio > inter:
        v_gremio+=1
    else:
        empate+=1
    
    grenais +=1
    
    print("Novo grenal (1-sim 2-nao)")
    v = int(input())


print(f'Teve {grenais} grenais')
print(f'O inter teve {v_inter} vitorias')
print(f'O gremio teve {v_gremio} vitorias')
print(f'O grenal teve {empate} empates')

if v_gremio > v_inter:
    print('O grêmio teve mais VITORIAS')
elif v_inter > v_gremio:
    print('O internacional teve mais VITORIAS')

elif v_gremio == v_inter:
    print('O grenal ficou EMPATE')
