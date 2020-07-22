def buscar_numero(vetor,numero,inicio,fim):
    if fim-inicio<=1:
        if vetor[fim-1]==numero:
            return fim-1
        else:
            try:
                return buscar_numero(vetor,numero,inicio,fim-1)
            except:
                return -1
    meio=int((fim-inicio)/2)
    if vetor[meio]<numero:
        return buscar_numero(vetor,numero,inicio+meio,fim)
    elif vetor[meio]>numero:
        return buscar_numero(vetor,numero,inicio,inicio+meio)
    elif vetor[meio]==numero:
        return meio
def main():
    vetor=input().split()
    x=len(vetor)
    for i in range(x):
        vetor[i]=int(vetor[i])
    i=int(input())
    print(buscar_numero(vetor,i,0,x))
main()
