def maximo(vetor,fim,inicio):
    if inicio==fim:
        return vetor[0]
    else:
        numero_comp=maximo(vetor,fim-1,inicio)
        if numero_comp>vetor[fim-1]:
            return numero_comp
        else:
            return vetor[fim-1]
def main():
    vetor_numeros=input().split()
    n=len(vetor_numeros)
    for i in range(n):
        vetor_numeros[i]=int(vetor_numeros[i])    
    print(maximo(vetor_numeros,n-1,0))
main()
