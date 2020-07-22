import sys
def labirinto(matriz,posicao=[],anterior=[]):
    if posicao==[]:
        for i in matriz[0]:
            if i=="E":
                posicao.append(0)
                posicao.append(matriz[0].index(i))
    prox_posicao=[(posicao[0]+1,posicao[1]),(posicao[0],posicao[1]+1),(posicao[0],posicao[1]-1),(posicao[0]-1,posicao[1])]#baixo,direita,esquerda,cima
    if not matriz[posicao[0]][posicao[1]]=="E":
            matriz[posicao[0]][posicao[1]]="x"
    for i in prox_posicao:
        x,y=i
        if matriz[x][y]=="S":
            anterior.append((posicao[0],posicao[1]))
            for j in anterior:
                a,b=j
                if not matriz[a][b]=="E":
                    matriz[a][b]="*"
            return matriz
        elif matriz[x][y]==" ":
            anterior.append((posicao[0],posicao[1]))
            posicao[0],posicao[1]=x,y
            return labirinto(matriz,posicao,anterior)
    posicao[0],posicao[1]=anterior[len(anterior)-1][0],anterior[len(anterior)-1][1]
    del(anterior[len(anterior)-1])
    return labirinto(matriz,posicao,anterior)
def main():
    x=[]
    for i in sys.stdin:
        x.append(i.strip())
    x = [[char for char in linha] for linha in x]
    x= labirinto(x)
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]=="x":
                x[i][j]=" "
    for a in x:
        print(''.join(a))
main()
