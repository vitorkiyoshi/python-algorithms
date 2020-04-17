def encontrarNum(conjuntoA, conjuntoB):
    repetidos=[]
    stringRep=""
    stringDel=""
    stringComp=""
    a=0
    c=0
    d=0
    for i in range(len(conjuntoA)):  #verificando repetidos em A e B
        for j in range(len(conjuntoB)):
            if conjuntoA[i]==conjuntoB[j]:
                repetidos.append(conjuntoA[i])
    while d==0:
        c=0
        for a in range(len(repetidos)-1,-1,-1):
            for b in range(len(repetidos)):
                if repetidos[a]==repetidos[b]: #verificacao de repeticao no vetor
                    c += 1
            if c>1:
                del(repetidos[a])
                break
            else:
                stringDel=stringDel+"1"+" "
            c=0
        for e in range(len(repetidos)):
            stringComp=stringComp+"1"+" "
        if stringComp==stringDel:
            d=1
        stringComp=""
        stringDel=""
    for x in range(len(repetidos)-1,-1,-1):
        if stringRep=="":
            stringRep=repetidos[x]
        else:
            stringRep=repetidos[x] + " " + stringRep
    print(stringRep)
A=input().split()
B=input().split()
encontrarNum(A,B);


