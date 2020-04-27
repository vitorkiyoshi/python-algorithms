ListaP=[]
seqProb=[]
seqNum=[]
def contar(x):
    for i in range(0,len(x)):
        if x[i] not in seqNum:
            seqNum.append(x[i])
def calcularProb(y):
    prob=0
    for j in range(0,len(ListaP)):
        if y==ListaP[j]:
           prob = prob + 1
    seqProb.append(prob)
def ordenar():
    for i in range(0,len(seqNum)):      #ordenando em ordem de prob
        for j in range(i+1,len(seqNum)):
            if int(seqNum[i])>int(seqNum[j]):#ordenação em crescente com condição da probabilidade
                if not seqProb[j]>seqProb[i]:
                    seqNum[j],seqNum[i]= seqNum[i],seqNum[j]
                    seqProb[j],seqProb[i]= seqProb[i],seqProb[j]
            if int(seqProb[i])>int(seqProb[j]): #ordenação de probabilidade
                seqNum[i],seqNum[j]= seqNum[j],seqNum[i]
                seqProb[i],seqProb[j]= seqProb[j],seqProb[i]
def main():
    L= input().split(' ')
    for i in range(0,len(L)):
        ListaP.append(int(L[i]))    #transforma em inteiros
    contar(ListaP)  #separa cada numero para contagem
    for i in range(0,len(seqNum)):
        calcularProb(seqNum[i])    #calcula quantas vezes apareceu tal numero
    ordenar()
    print(*seqNum)
main()


