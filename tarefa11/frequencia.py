from operator import itemgetter
def carregar_texto(nome_de_arquivo):
    texto = []
    with open(nome_de_arquivo) as arquivo:
        for linha in arquivo:
            texto.extend(linha.strip().split())
    for i in range(len(texto)):
        if texto[i][len(texto[i])-1]=="," or texto[i][len(texto[i])-1]=="." or texto[i][len(texto[i])-1]=="?": #retirando caracteres que possam atrapalhar
            texto[i]=texto[i][0:len(texto[i])-1]
        if texto[i][len(texto[i])-1]=="\'":
            if texto[i][len(texto[i])-3]=="," or texto[i][len(texto[i])-3]==".":
                texto[i]=texto[i][0:len(texto[i])-3]
            else:
                texto[i]=texto[i][0:len(texto[i])-2]
        if texto[i][0]=="\'":
            texto[i]=texto[i][2:len(texto[i])]
    return texto
def retirar_stopWords(texto,stopWords):
    k=0
    texto_sem_stopWords=list(texto)
    for i in range(len(texto)):
        for j in range(len(stopWords)):
            if stopWords[j]==texto[i].lower():
                texto_sem_stopWords[i]=''
    while k<=len(texto_sem_stopWords)-1:
        if texto_sem_stopWords[k]=='':
            del(texto_sem_stopWords[k])
            k=0
        else:
            k+=1
    return texto_sem_stopWords
def calcular_frequencia(texto):
    frequencia=[]
    txt_sem_repeticao=[]
    freq_palavra=0
    for i in range(len(texto)):
        if texto[i].lower() not in txt_sem_repeticao:
            txt_sem_repeticao.append(texto[i].lower())
    for k in range(len(txt_sem_repeticao)):
        for j in range(len(texto)):
            if txt_sem_repeticao[k] == texto[j].lower():
                freq_palavra += 1
        frequencia.append((txt_sem_repeticao[k], freq_palavra))
        freq_palavra = 0
    frequencia = sorted(sorted(frequencia, key=itemgetter(0)),key=itemgetter(1),reverse=True)#primeiro sort ordem alfabetica, segundo por ordem de freq
    return frequencia
def calcular_quartil(ordenadas):
    nao_incluidos=[]
    quartil=[]
    numero_palavras=0
    for i in range(len(ordenadas)):
        if not ordenadas[i][1]<5:
            quartil.append((ordenadas[i][0],ordenadas[i][1]))    #retirando <5 a freq
        else:
            nao_incluidos.append(ordenadas[i])
    posicao_quartil = int(0.25 * (len(quartil))-1)
    for i in range(len(quartil)):
        if quartil[i][1]>=quartil[posicao_quartil][1]:
            numero_palavras+=1
        else:
            nao_incluidos.append(quartil[i])
    nao_incluidos=sorted(nao_incluidos, key=itemgetter(1) , reverse=True)
    print(numero_palavras)
    print(nao_incluidos[0][0]+" "+nao_incluidos[1][0]+" "+nao_incluidos[2][0])
    pass
def main():
    texto=carregar_texto(input())
    stop_words=input().split()
    texto=retirar_stopWords(texto,stop_words)
    frequencias=calcular_frequencia(texto)
    print(frequencias[0][0]+" "+frequencias[1][0]+" "+frequencias[2][0])
    calcular_quartil(frequencias)
main()
