def filtra(f,lista):
    filtrado=[]
    for i in range(len(lista)):
        if f(lista[i])==True:
            filtrado.append(lista[i])
    return filtrado     
def mapeia(f,lista):
    novaLista=[]
    for i in range(len(lista)):
        novaLista.append(f(lista[i]))
    return novaLista
def reduz(f,lista):
    if not(lista==[]):
        x=lista[0]
        for i in range(len(lista)-1):
            x=f(x,lista[i+1])
        return x
    else:
        return 0
def primo(x):
    n=x
    div=0
    while(n>0):
        if x%n==0:
            div+=1
        n-=1
    if div==2:
        return True
    else:
        return False
def quadrado(x):
    return x**2
def somar(x,y):
    return x+y
def convInt(x):
    return int(x)
def main():
    lista=mapeia(convInt,input().split())
    print(reduz(somar,mapeia(quadrado,filtra(primo,lista))))
main()
