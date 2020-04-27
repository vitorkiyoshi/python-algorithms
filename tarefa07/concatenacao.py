textoA=input().split(" ")
textoB=input().split(" ")
textoC=[]
for i in range(len(textoA)):
    textoC.append(textoA[i]+textoB[i])

print(*textoC)
