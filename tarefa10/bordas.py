from modulo import *


def destacar_bordas(largura, altura, imagem):
    ImagemOriginal=[[0 for _ in range(largura)] for _ in range(altura)]
    for i in range(len(ImagemOriginal)):
        for j in range(len(ImagemOriginal[i])):
            ImagemOriginal[i][j]=imagem[i][j]
    for i in range(1, altura - 1, +1):
        for j in range(1, largura - 1, +1):
            igualdade = 0
            if ImagemOriginal[i][j] == '1':
                if ImagemOriginal[i+1][j]== '1':
                    igualdade += 1
                if ImagemOriginal[i+1][j+1]== '1':
                    igualdade += 1
                if ImagemOriginal[i][j+1] == '1':
                    igualdade += 1
                if ImagemOriginal[i-1][j+1] == '1':
                    igualdade += 1
                if ImagemOriginal[i-1][j]=='1':
                    igualdade += 1
                if ImagemOriginal[i-1][j-1]=='1':
                    igualdade += 1
                if ImagemOriginal[i][j-1]=='1':
                    igualdade += 1
                if ImagemOriginal[i+1][j-1] == '1':
                    igualdade +=1
                if igualdade==8:
                    imagem[i][j]='0'
    return imagem


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
