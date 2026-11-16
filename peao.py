from tabuleiro import posicao_valida
#MÓDULO INTEGRANTE 4: peça e controle de turnos

#VARIÁVEIS GLOBAIS
peao_preto = '♙' #desenho que representa o peão preto dentro da matriz
peao_branco = '♟' #desenho que representa o peão branco dentro da matriz

pecas_pretas = ['♖', '♘', '♗', '♕', '♔', '♙'] #desenhos de todas as peças de cor preta
pecas_brancas = ['♜', '♞', '♝', '♛', '♚', '♟'] #desenhos de todas as peças de cor branca

def movimento_peao(tabuleiro, origem, destino):
    """
    Realiza os movimentos e capturas dos peões
    
    Parâmetros: 
        tabuleiro (lista): matriz 8x8 que guarda as peças e casas vazias
        origem (tupla): guarda a posição da linha e coluna da peça escolhida
        destino (tupla): guarda a posição da linha e coluna do destino da peça

    Return: 
        bool
    """
    #garante que todas as variáveis irão existir mesmo se uma delas for falsa
    avanco = False
    avanco_duplo = False
    captura = False

    #recebe o valor da origem e destino escolhidos pelo jogador
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    #não roda a função se a posição escolhida for inválida
    if not posicao_valida(linha_origem, coluna_origem, linha_destino, coluna_destino):
        return False

    #guarda a origem e o destino da peça
    casa_origem = tabuleiro[linha_origem][coluna_origem] 
    casa_destino = tabuleiro[linha_destino][coluna_destino] 

    #fórmulas para calcular a quantidade de avanço de casas da origem para o destino
    diferenca_linha = linha_destino - linha_origem
    diferenca_coluna = coluna_destino - coluna_origem

   #AVANÇOS
    if casa_origem == peao_preto and casa_destino == ' ': 
        if (diferenca_linha == 1) and (diferenca_coluna == 0): #avança uma casa
            avanco = True 
        elif linha_origem == 1 and (diferenca_linha == 2) and (diferenca_coluna == 0) and tabuleiro[linha_destino - 1][coluna_destino] == ' ': #avança duas casas
            avanco_duplo = True

    if casa_origem == peao_branco and casa_destino == ' ': 
        if (diferenca_linha == -1) and (diferenca_coluna == 0): #avança uma casa
            avanco = True 
        elif linha_origem == 6 and (diferenca_linha == -2) and (diferenca_coluna == 0) and tabuleiro[linha_destino + 1][coluna_destino]  == ' ': #avança duas casas
            avanco_duplo = True 

    #CAPTURA NA DIAGONAL
    #pretas
    if casa_origem == peao_preto and (((diferenca_linha == 1) and (diferenca_coluna == 1)) or ((diferenca_linha == 1) and (diferenca_coluna == -1))) and casa_destino in pecas_brancas:
        captura = True 
    #brancas
    elif casa_origem == peao_branco and (((diferenca_linha == -1) and (diferenca_coluna == 1)) or ((diferenca_linha == -1) and (diferenca_coluna == -1))) and casa_destino in pecas_pretas:
        captura = True

    #RETORNA A CONDIÇÃO CASO SEJA VERDADEIRA PARA O MAIN
    if avanco or avanco_duplo or captura:
        return True
    else:
        return False

def promocao_peao(tabuleiro, destino): #Não estava no escopo inicial do projeto, porém quis acrescentar essa regra, pois faz parte das regras oficiais (Luana)
    """
    Realiza a promoção do peão para que se torne a nova peça definida pelo usuário
    
    Parâmetros: 
        tabuleiro (lista): matriz 8x8 que guarda as peças e casas vazias
        destino (tupla): guarda a posição da linha e coluna do destino da peça

    Return: 
        sem retorno
    """ 
    linha_destino, coluna_destino = destino #recebe o valor do destino escolhido pelo jogador
    casa_destino = tabuleiro[linha_destino][coluna_destino] #guarda a peça que foi para o destino escolhido
    
    #TROCA O PEÃO POR OUTRA PEÇA
    if (linha_destino == 7 and casa_destino == peao_preto) or (linha_destino == 0 and casa_destino == peao_branco):
        while True:
            try:
                pergunta = int(input('Por qual peça você deseja trocar o peão?\nEscolha o número correspondente a peça:\nTorre = 1\nCavalo = 2\nBispo = 3\nDama = 4\nDigite a opção escolhida:'))
                if 1 <= pergunta <= 4:
                    if casa_destino == peao_preto:
                        tabuleiro[linha_destino][coluna_destino] = pecas_pretas[pergunta - 1] #muda para a peça escolhida
                        break
                    elif casa_destino == peao_branco:
                        tabuleiro[linha_destino][coluna_destino] = pecas_brancas[pergunta - 1]
                        break
                else:
                    print('Ops! Opção inválida! Digite um número de 1 a 4\n Opção escolhida:')

            except ValueError: #mostra uma mensagem de erro caso a pessoa digite um caractere ou letra
                print('Ops! Opção inválida! Digite um número de 1 a 4\n Opção escolhida:')

def controlar_turno(tabuleiro, origem, turno): 
    """
    Fiscaliza se a peça escolhida é da cor correspondente de acordo com o jogador do turno atual
    
    Parâmetros:
        tabuleiro (lista): matriz 8x8 que guarda as peças e casas vazias
        origem (tupla): guarda a posição da linha e coluna da peça escolhida
        turno (str): cor de quem está jogando agora

    Return:
        bool
     
    """ 
    linha_origem, coluna_origem = origem #recebe o valor da origem escolhida pelo jogador

    peca = tabuleiro[linha_origem][coluna_origem] #guarda a peça ou casa vazia da matriz

    if (peca in pecas_brancas and turno == 'brancas') or (peca in pecas_pretas and turno == 'pretas'):
        return True
    else:
        return False
    
def trocar_turno(turno):
    """
    Passa a vez para o próximo jogador

    Parâmetros: 
        turno(str): cor de quem está jogando agora

    Return:
        str: cor de quem joga em seguida ('pretas' ou 'brancas')
     
    """ 
    if turno == 'brancas':
        return 'pretas'
    elif turno == 'pretas':
        return 'brancas'
    else:
        return None
