from modulo import carregar_imagem_decodificada

def testar_leitura_pbm():
    largura, altura, imagem = carregar_imagem_decodificada("testes/jota.pbm")
    assert largura == 6
    assert altura == 10
    matriz_esperada = [
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['1', '0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
    ]
    assert imagem == matriz_esperada

testar_leitura_pbm()