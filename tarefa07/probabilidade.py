def contar(x):
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            if x[i]==x[j] and x[i] not in seqNum:
                seqNum.append(x[i])
def calcularProb(y):
    prob=0
    for j in range(0,len(ListaP)):
        if y==ListaP[j]:
           prob = prob + 1
    seqProb.append(prob)
ListaP=[]
seqProb=[]
seqNum=[]
L= input().split(' ')
for i in range(0,len(L)):
    ListaP.append(int(L[i]))    #transforma em inteiros
contar(ListaP)  #separa cada numero para contagem
for i in range(0,len(seqNum)):
    calcularProb(seqNum[i])    #calcula quantas vezes apareceu tal numero
for i in range(0,len(seqNum)):      #ordenando em ordem de prob
    for j in range(0,len(seqNum)):
        if int(seqProb[j])>int(seqProb[i]):
            seqNum[j],seqNum[i]= seqNum[i],seqNum[j]
            seqProb[j],seqProb[i]= seqProb[i],seqProb[j]
for i in range(0,len(seqNum)):      #ordenando em ordem crescente os termos separados
    for j in range(0,len(seqNum)):
        if(j>i): #apenas trocando com os próximos números da lista
            if int(seqNum[i])>int(seqNum[j]):
                if not seqProb[j]>seqProb[i]:
                    seqNum[j],seqNum[i]= seqNum[i],seqNum[j]
                    seqProb[j],seqProb[i]= seqProb[i],seqProb[j]
print(*seqNum)
