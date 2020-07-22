def menor_ausente(vetor,posicao):
    x=(vetor[posicao]+vetor[posicao+2])/2
    if not x==vetor[posicao+1]:
        y=vetor[posicao]+2
        return y
    else:
        return menor_ausente(vetor,posicao+1)
def main():
    vetor_numeros=input().split()
    for i in range(len(vetor_numeros)):
        vetor_numeros[i]=int(vetor_numeros[i])
    print(menor_ausente(vetor_numeros,0))
main()
