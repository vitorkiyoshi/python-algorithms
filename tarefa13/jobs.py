retorno=[]
while True:
    try:
        numeros=[]
        n=int(input())
        soma=0
        numeros=input().split()
        numeros=[int(i) for i in numeros]
        somatorio=sum(numeros)
        for i in numeros:
            if soma+i<=somatorio/2:
                soma+=i
            else:
                retorno.append(min(-somatorio+2*(soma+i),somatorio-2*(soma)))
                break
    except:
        for i in retorno:
            print(str(i))
        break
