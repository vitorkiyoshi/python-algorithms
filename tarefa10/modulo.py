def codificar(largura, altura, imagem):
    # com largura e altura se sabe o tamanho da imagem, imagem é matriz[altura][largura]
    bits = []
    codigo=[]
    posicao=0
    codificacao = ""
    for i in range(0,altura-1,+2):
        for j in range(largura):
            bits.append(str(imagem[i][j])+str(imagem[i+1][j]))  #vetor bits com pares segundo run-length
    while posicao <= altura*largura/2 - 1:
        qtde,posicao = contar(bits, posicao)#conta bits iguais até o próximo, mudando a posicao para o proximo contador
        codigo.append(str(qtde)) #vetor com qtde do elemento seguido do elemento
        codigo.append(str(bits[posicao]))
        posicao += 1
    for i in range(len(codigo)): #transformando codigo em string
        if i!=len(codigo):
            codificacao += codigo[i] + " "
        else:
            codificacao += codigo[i]
    return codificacao
def contar(vetor, valor):
    i = True
    contador = 1
    while i:
        if valor<(len(vetor)-1) and vetor[valor] == vetor[valor + 1]:
            contador += 1
            valor+=1
        else:
            i = False
    return contador,valor #retorna conta e onde fica a ultima repeticao
def decodificar(largura, altura, codificacao):
    bits=[]
    imagem = [[0 for _ in range(largura)] for _ in range(altura)] #definindo tamanho da matriz
    posicaoVetor=0
    for i in range(0,len(codificacao)-1,+2):
        for j in range(int(codificacao[i])):
            bits.append(codificacao[i+1]) #fazendo um vetor com os pares de bits
    for i in range(0,altura-1,+2):
        for j in range(largura):
            imagem[i][j], imagem[i+1][j]=bits[posicaoVetor][0],bits[posicaoVetor][1] #transformando vetor na imagem
            posicaoVetor+=1
    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        formato=next(arquivo)
        tamanho=next(arquivo).split()
        largura=int(tamanho[0])
        altura=int(tamanho[1])
        codificacao=arquivo.readline().split()
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        linhas=[]
        for linha in arquivo:
            linhas.append(linha)
        tamanho=linhas[1].split()
        largura= int(tamanho[0])
        altura=int(tamanho[1])
        imagem = [[0 for _ in range(largura)] for _ in range(altura)] #definindo tamanho da matriz
        for i in range(altura):
            for j in range(largura):
                imagem[i][j]=linhas[i+2][j]
    return largura, altura, imagem

def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write("P1C" + "\n")
        arquivo.write(str(largura) + " " + str(altura) + "\n")
        arquivo.write(codificacao)
    pass


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write("P1" + "\n")
        arquivo.write(str(largura) + " " + str(altura) + "\n")
        for i in range(altura):
            for j in range(largura):
                arquivo.write(imagem[i][j])
            arquivo.write("\n")
    pass
