
from tabuleiro import posicao_valida, mover_peca

# MÓDULO INTEGRANTE 3: Peças especiais e sistema de capturas

# Listas das peças de acordo com as cores definidas no projeto
PECAS_PRETAS = ['♖', '♘', '♗', '♕', '♔', '♙']
PECAS_BRANCAS = ['♜', '♞', '♝', '♛', '♚', '♟']

# Identificação das peças de movimento especial
REIS = ('♔', '♚')
CAVALOS = ('♘', '♞')


def movimento_rei(tabuleiro, origem, destino):
    """
    Verifica se o movimento do rei é válido.
    O rei pode andar uma casa em qualquer direção.

    Parâmetros:
        tabuleiro (lista): matriz 8x8 do jogo
        origem (tupla): linha e coluna da peça escolhida
        destino (tupla): linha e coluna do destino

    Return:
        bool
    """

    # Recebe as coordenadas de origem e destino
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Verifica se as posições estão dentro do tabuleiro
    if not posicao_valida(linha_origem, coluna_origem):
        return False

    if not posicao_valida(linha_destino, coluna_destino):
        return False

    # Guarda a peça presente na casa de origem
    peca_origem = tabuleiro[linha_origem][coluna_origem]

    # Verifica se a peça escolhida é um rei
    if peca_origem not in REIS:
        return False

    # Impede que a peça permaneça na mesma posição
    if origem == destino:
        return False

    # Calcula a quantidade de casas percorridas
    diferenca_linha = abs(linha_destino - linha_origem)
    diferenca_coluna = abs(coluna_destino - coluna_origem)

    # MOVIMENTO DO REI: uma casa em qualquer direção
    if diferenca_linha <= 1 and diferenca_coluna <= 1:
        return True
    else:
        return False


def movimento_cavalo(tabuleiro, origem, destino):
    """
    Verifica se o movimento do cavalo é válido.
    O cavalo realiza movimentos em formato de L.

    Parâmetros:
        tabuleiro (lista): matriz 8x8 do jogo
        origem (tupla): linha e coluna da peça escolhida
        destino (tupla): linha e coluna do destino

    Return:
        bool
    """

    # Recebe as coordenadas de origem e destino
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Verifica se as posições estão dentro do tabuleiro
    if not posicao_valida(linha_origem, coluna_origem):
        return False

    if not posicao_valida(linha_destino, coluna_destino):
        return False

    # Guarda a peça presente na casa de origem
    peca_origem = tabuleiro[linha_origem][coluna_origem]

    # Verifica se a peça escolhida é um cavalo
    if peca_origem not in CAVALOS:
        return False

    # Calcula a quantidade de casas percorridas
    diferenca_linha = abs(linha_destino - linha_origem)
    diferenca_coluna = abs(coluna_destino - coluna_origem)

    # MOVIMENTO EM L:
    # Duas casas na vertical e uma na horizontal
    movimento_vertical = (diferenca_linha == 2 and
                          diferenca_coluna == 1)

    # Uma casa na vertical e duas na horizontal
    movimento_horizontal = (diferenca_linha == 1 and
                            diferenca_coluna == 2)

    # O cavalo pode saltar sobre outras peças,
    # portanto não é necessário verificar o caminho
    if movimento_vertical or movimento_horizontal:
        return True
    else:
        return False


def mesma_cor(peca_origem, peca_destino):
    """
    Verifica se duas peças pertencem à mesma cor.

    Parâmetros:
        peca_origem (str): símbolo da peça de origem
        peca_destino (str): símbolo da peça de destino

    Return:
        bool
    """

    # Verifica se as duas peças são pretas
    if peca_origem in PECAS_PRETAS and peca_destino in PECAS_PRETAS:
        return True

    # Verifica se as duas peças são brancas
    elif peca_origem in PECAS_BRANCAS and peca_destino in PECAS_BRANCAS:
        return True

    # Peças de cores diferentes ou casas vazias
    else:
        return False


def captura_permitida(tabuleiro, origem, destino):
    """
    Verifica se a captura é permitida considerando
    as posições e as cores das peças.

    Parâmetros:
        tabuleiro (lista): matriz 8x8 do jogo
        origem (tupla): linha e coluna da peça escolhida
        destino (tupla): linha e coluna do destino

    Return:
        bool
    """

    # Recebe as coordenadas de origem e destino
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Verifica se as posições estão dentro do tabuleiro
    if not posicao_valida(linha_origem, coluna_origem):
        return False

    if not posicao_valida(linha_destino, coluna_destino):
        return False

    # Guarda o conteúdo das casas de origem e destino
    peca_origem = tabuleiro[linha_origem][coluna_origem]
    peca_destino = tabuleiro[linha_destino][coluna_destino]

    # Verifica se existe uma peça válida na origem
    if peca_origem not in PECAS_PRETAS + PECAS_BRANCAS:
        return False

    # Verifica se existe uma peça válida no destino
    # Não existe captura quando a casa está vazia
    if peca_destino not in PECAS_PRETAS + PECAS_BRANCAS:
        return False

    # Impede a captura de peças da mesma cor
    if mesma_cor(peca_origem, peca_destino):
        return False

    # Impede a captura direta do rei adversário
    # No xadrez, o rei não pode ser capturado
    if peca_destino in REIS:
        return False

    # A captura é permitida quanto à ocupação e à cor
    return True


def capturar_peca(tabuleiro, origem, destino):
    """
    Captura uma peça adversária e atualiza o tabuleiro.

    A movimentação da peça deve ter sido validada
    antes de chamar esta função.

    Parâmetros:
        tabuleiro (lista): matriz 8x8 do jogo
        origem (tupla): linha e coluna da peça escolhida
        destino (tupla): linha e coluna da peça capturada

    Return:
        bool
    """

    # Verifica se a captura é permitida
    if not captura_permitida(tabuleiro, origem, destino):
        return False

    # Utiliza a função existente no módulo tabuleiro
    # A peça de origem substitui a peça adversária
    # A casa de origem passa a ficar vazia
    mover_peca(tabuleiro, origem, destino)

    # Confirma que a captura foi realizada
    return True

