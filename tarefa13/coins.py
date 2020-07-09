N=float(input())
cedulas={'100.00':0,'50.00':0,'20.00':0,'10.00':0,'5.00':0,'2.00':0}
moedas={'1.00':0,'0.50':0,'0.25':0,'0.10':0,'0.05':0,'0.01':0}
qtde=0
for i in cedulas:
    qtde=int(N/float(i))
    N-=(qtde*float(i))    
    cedulas[i]=qtde
for i in moedas:
    qtde=int(N/float(i))
    N-=(qtde*float(i))    
    moedas[i]=qtde
print("NOTAS:")
for i in cedulas:
    if not cedulas[i]==0:
            print(str(cedulas[i])+" nota(s) de R$ "+str(i))
if sum(moedas.values())>0:
    print("MOEDAS:")
    for i in moedas:
        if not moedas[i]==0:
            print(str(moedas[i])+" moeda(s) de R$ "+str(i))
