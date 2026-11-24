from tabuleiro import posicao_valida
#### OBS: não foi feito revisão ainda, é só um esboço
#peças: rei, cavalo -> funções: movimento_rei(), movimento_cavalo()
#implementar: mesma_cor(), captura_permitida(), capturar_peca()
#impedir captura de peça da msm cor; permitir captura de peças adversárias; atualizar o tabuleiro após captura

def movimento_rei(tabuleiro, origem, destino):
    """
    Realiza o movimento do rei e do ##roque

    Parâmetros:
        tabuleiro
        origem
        destino

    Return:
        bool
    """
    d_linha = l_destino - l_origem #d = diferença, l = linha, c = coluna
    d_coluna = c_destino - c_origem # d = diferença, l = linha, c = coluna

    rei_preto = '♔'
    rei_branco = '♚'
    #MOVIMENTO PADRÃO: uma casa de cada vez em qualquer direção
    if casa_origem == peca in('♔', '♚'): 
        if d_linha <= 1 and d_coluna <= 1: 
            return True
        else: 
            return False
            
    #MOVIMENTO ROQUE: torre protege o rei SE rei e torre estiver na posição inicial e SE o rei andar duas casas na direção da torre
    #if rei_preto == casa_origem[0][4] and torre == casa_origem[0][0]: #roque grande
    #    if rei_preto == (l_destino == 0 and c_destino == 2):
    #        torre_protege = casa_origem[0][0]
    #        casa_destino[0][3] = torre_protege
    #        casa_origem[0][0] = ' '
    #elif rei_branco == casa_origem[7][4] and torre == casa_origem[7][7]: #roque pequeno
    #    if rei_branco == (l_destino == 7] and c_destino == 5):
     #       torre_protege = casa_origem[7][7]:
      #      casa_destino[7][5] = torre_protege
       #     casa_origem[7][7] = ' '
        
def movimento_cavalo(tabuleiro, origem, destino):
    """
    Realiza o movimento do cavalo

    Parâmetros:
        tabuleiro
        origem
        destino

    Return:
        bool
    """
    cavalo = '♘' or '♞'
#movimento em L (única peça que pode saltar sobre outras peças)
    if casa_origem == cavalo:
        if ((d_linha == -2) and (d_coluna in (-1, 1)) or ((d_linha == 2) and (d_coluna in (-1, 1)) or ((d_linha == -1) and (d_coluna in (-2, 2)) or ((d_linha == 1) and (d_coluna in (-2,2)):
            peca_move = True
        
def mesma_cor(tabuleiro):
    """
    Guarda a lista das cores de cada peça

    Parâmetros:
        tabuleiro
    
    Return:
        pecas_pretas, pecas_brancas
    """
    
    pecas = ['♖', '♘', '♗', '♕', '♔', '♙', '♜', '♞', '♝', '♛', '♚', '♟']                                                                                                                                       
    pecas_pretas = ['♖', '♘', '♗', '♕', '♔', '♙'] #desenhos de todas as peças de cor preta
    pecas_brancas = ['♜', '♞', '♝', '♛', '♚', '♟'] #desenhos de todas as peças de cor branca
               
    return pecas_pretas, pecas_brancas

def captura_permitida(tabuleiro, origem, destino, posicao_valida):
    """
    Permite a captura se a posição for válida e se o destino for uma peça

    Parâmetros:
        tabuleiro
        origem
        destino

    Return:
        bool
    """
    casa_origem = tabuleiro[linha_origem][coluna_origem]
    casa_destino = tabuleiro[linha_destino][coluna_destino]
    
    if posicao_valida == True:
        if casa_destino == 'peca_preta':
            return True
        elif casa_destino == 'peca_branca':
            return True
        else:
            return False

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
    if (pecas_pretas == origem and pecas_brancas == destino) or (pecas_brancas == origem and pecas_pretas == destino)):
        captura = tabuleiro[linha_origem][coluna_origem]
        tabuleiro[linha_destino][coluna_destino] = captura
        tabuleiro[linha_origem][coluna_origem] = ''
        return True
    else: #não captura peça da mesma cor 
        return False 
