from bordas import destacar_bordas


def testar_bordas():
    # crie um exemplo de imagem pequena para testar
    largura = ...
    altura = ...
    imagem = [
        ...
    ]

    # cria a matriz de bordas que você espera para essa imagem
    bordas_esperadas = [
        ...
    ]

    # aqui chamamos a função sendo testada
    bordas_calculadas = destacar_bordas(largura, altura, imagem)

    # isso irá gerar um erro quando a função não estiver correta
    assert bordas_esperadas == bordas_calculadas

    # se o programa não falhou, então talvez sua função esteja correta


testar_bordas()
