from tabuleiro import posicao_valida

# peças de movimento(Torre, Bispo e Dama)

PECAS_PRETAS = ['♖', '♘', '♗', '♕', '♔', '♙']
PECAS_BRANCAS = ['♜', '♞', '♝', '♛', '♚', '♟']
TORRES = ('♖', '♜')
BISPOS = ('♗', '♝')
DAMAS = ('♕', '♛')


def caminho_livre(tabuleiro, origem, destino):
    """
    Verifica se não há peças bloqueando o caminho entre origem e destino.
    """
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not posicao_valida(linha_origem, coluna_origem) or not posicao_valida(linha_destino, coluna_destino):
        return False

    if (linha_origem, coluna_origem) == (linha_destino, coluna_destino):
        return False

    diferenca_linha = linha_destino - linha_origem
    diferenca_coluna = coluna_destino - coluna_origem

    if diferenca_linha > 0:
        passo_linha = 1
    elif diferenca_linha < 0:
        passo_linha = -1
    else:
        passo_linha = 0

    if diferenca_coluna > 0:
        passo_coluna = 1
    elif diferenca_coluna < 0:
        passo_coluna = -1
    else:
        passo_coluna = 0

    linha_atual = linha_origem + passo_linha
    coluna_atual = coluna_origem + passo_coluna

    while (linha_atual, coluna_atual) != (linha_destino, coluna_destino):
        if tabuleiro[linha_atual][coluna_atual] != ' ':
            return False
        linha_atual += passo_linha
        coluna_atual += passo_coluna

    return True


def movimento_torre(tabuleiro, origem, destino):
    """
    Verifica se o movimento da torre é válido (linha reta e sem bloqueios).
    """
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not posicao_valida(linha_origem, coluna_origem) or not posicao_valida(linha_destino, coluna_destino):
        return False

    peca_origem = tabuleiro[linha_origem][coluna_origem]
    if peca_origem not in TORRES:
        return False

    if (linha_origem, coluna_origem) == (linha_destino, coluna_destino):
        return False

    mesma_linha = (linha_origem == linha_destino)
    mesma_coluna = (coluna_origem == coluna_destino)

    if not (mesma_linha or mesma_coluna):
        return False

    return caminho_livre(tabuleiro, origem, destino)


def movimento_bispo(tabuleiro, origem, destino):
    """
    Verifica se o movimento do bispo é válido (diagonal e sem bloqueios).
    """
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not posicao_valida(linha_origem, coluna_origem) or not posicao_valida(linha_destino, coluna_destino):
        return False

    peca_origem = tabuleiro[linha_origem][coluna_origem]
    if peca_origem not in BISPOS:
        return False

    if (linha_origem, coluna_origem) == (linha_destino, coluna_destino):
        return False

    diferenca_linha = linha_destino - linha_origem
    diferenca_coluna = coluna_destino - coluna_origem

    if abs(diferenca_linha) != abs(diferenca_coluna):
        return False

    return caminho_livre(tabuleiro, origem, destino)


def movimento_dama(tabuleiro, origem, destino):
    """
    Verifica se o movimento da dama é válido (linha reta ou diagonal, sem bloqueios).
    """
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not posicao_valida(linha_origem, coluna_origem) or not posicao_valida(linha_destino, coluna_destino):
        return False

    peca_origem = tabuleiro[linha_origem][coluna_origem]
    if peca_origem not in DAMAS:
        return False

    if (linha_origem, coluna_origem) == (linha_destino, coluna_destino):
        return False

    diferenca_linha = linha_destino - linha_origem
    diferenca_coluna = coluna_destino - coluna_origem

    movimento_reto = (linha_origem == linha_destino) or (coluna_origem == coluna_destino)
    movimento_diagonal = (abs(diferenca_linha) == abs(diferenca_coluna))

    if not (movimento_reto or movimento_diagonal):
        return False

    return caminho_livre(tabuleiro, origem, destino)