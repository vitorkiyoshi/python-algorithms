def kesimo(vetor,posicao,contador):
    x = vetor[vetor.index(min(vetor))]
    if contador==posicao-1:
        return x
    else:
        del(vetor[vetor.index(min(vetor))])
        return kesimo(vetor,posicao,contador+1)
def main():
    numeros=input().split()
    for i in range(len(numeros)):
        numeros[i]=int(numeros[i])
    print(kesimo(numeros,int(input()),0))
main()
