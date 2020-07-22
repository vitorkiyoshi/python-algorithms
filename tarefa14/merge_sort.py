def intercalar(lista1,lista2,acum=None):
    if acum is None:
        acum = []
    i=0
    j=0
    while i<len(lista1) and j<len(lista2):
        if lista1[i]<lista2[j]:
            acum.append(lista1[i])
            i+=1
        else:
            acum.append(lista2[j])
            j+=1
    if j<len(lista2):
        while j<len(lista2):
            acum.append(lista2[j])
            j+=1
    if i<len(lista1):
        while i<len(lista1):
            acum.append(lista1[i])
            i+=1
    return acum
def merge_sort(lista,inicio,fim):
    if inicio==fim:
        return [lista[fim]]
    if inicio<fim:
        meio=(inicio+fim)//2
        a = merge_sort(lista,inicio,meio)
        b = merge_sort(lista,meio+1,fim)
        return intercalar(a,b)
def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    y=merge_sort(lista,0,len(lista)-1)
    print(*y)
main()
