from tabuleiro import posicao_valida

#peças: rei, cavalo -> funções: movimento_rei(), movimento_cavalo()
#implementar: mesma_cor(), captura_permitida(), capturar_peca()
#impedir captura de peça da msm cor; permitir captura de peças adversárias; atualizar o tabuleiro após captura

def mesma_cor():
    """
    Guarda a lista das cores de cada peça

    Parâmetros:
        sem parâmetros
    
    Return:
        pecas_pretas, pecas_brancas
    """
    pecas_pretas = ['♖', '♘', '♗', '♕', '♔', '♙'] #desenhos de todas as peças de cor preta
    pecas_brancas = ['♜', '♞', '♝', '♛', '♚', '♟'] #desenhos de todas as peças de cor branca
    return pecas_pretas, pecas_brancas

def captura_permitida(tabuleiro, origem, destino):
    """
    Permite a captura
    """
    casa_origem = tabuleiro[linha_origem][coluna_origem]
    casa_destino = tabuleiro[linha_destino][coluna_destino]

    if casa_destino == '':
        return False
    elif casa_destino 


def captura_peca(tabuleiro, origem, destino, posicao_valida):
    """
    Captura a peça adversária e atualiza o tabuleiro

    Parâmetros:
        tabuleiro
        origem
        destino
        posicao_valida

    Return:
        bool
    """
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # capturas permitidas para peças adversárias
    if posicao_valida == True and ((pecas_pretas == origem and pecas_brancas == destino) or (pecas_brancas == origem and pecas_pretas == destino)):
        captura = tabuleiro[linha_origem][coluna_origem]
        tabuleiro[linha_destino][coluna_destino] = captura
        tabuleiro[linha_origem][coluna_origem] = ''
        return True
    else: #não captura peça da mesma cor 
        return False 
