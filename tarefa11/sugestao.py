from operator import itemgetter
def carregar_texto(nome_do_arquivo):
    texto=[]
    with open(nome_do_arquivo) as arquivo:
        for linha in arquivo:
            texto.extend(linha.strip().split())
    for i in range(len(texto)):
        if texto[i][len(texto[i])-1]=="\'":
            if texto[i][len(texto[i])-3]=="," or texto[i][len(texto[i])-3]==".":
                texto[i]=texto[i][0:len(texto[i])-3]
            else:
                texto[i]=texto[i][0:len(texto[i])-2]
        if texto[i][len(texto[i])-1]=="," or texto[i][len(texto[i])-1]=="." or texto[i][len(texto[i])-1]=="?": #retirando caracteres que possam atrapalhar
            if texto[i][len(texto[i])-2]=="\'":
                texto[i]=texto[i][0:len(texto[i])-3]
            else:
                texto[i]=texto[i][0:len(texto[i])-1]
        if texto[i][0]=="\'":
            texto[i]=texto[i][2:len(texto[i])]    
    return texto
def apresentar_sugestao(par,texto):
    palavras=[]
    pal_sem_rep=[]
    sugestoes=[]
    freq=0
    for a in range(len(par)):
        for pos in range(len(texto)-2):
            if par[0]==texto[pos].lower() and par[1]==texto[pos+1].lower():
                palavras.append(texto[pos+2].lower())
    for i in range(len(palavras)):
        if not palavras[i] in pal_sem_rep:
            pal_sem_rep.append(palavras[i])
    for i in range(len(pal_sem_rep)):
        for j in range(len(palavras)):
            if pal_sem_rep[i]==palavras[j]:
                freq+=1
        sugestoes.append((pal_sem_rep[i],freq))
        freq=0
    sugestoes=sorted(sorted(sugestoes, key=itemgetter(0)),key=itemgetter(1),reverse=True)
    print(par[0]+" "+par[1]+" "+sugestoes[0][0])
def main():
    texto=carregar_texto(input())
    sequencia=[]
    while True:
        try:
            sequencia.append(input().split())
        except:
            break
    for i in range(len(sequencia)):
        apresentar_sugestao(sequencia[i],texto)
main()
