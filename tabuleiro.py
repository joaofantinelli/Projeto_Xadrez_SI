#MÓDULO 0: main -> arquivo principal
def main ():
    """
    Cria as informações iniciais para começar o jogo e guarda as variáveis locais
    """
    print("=" * 11, "JOGO DE XADREZ", "=" * 11)
    print(" ")

    criado = criar_tabuleiro() #a variável está chamando a função que mostra o tabuleiro criado
    mostrar_tabuleiro(criado) #mostra a variável "criado" que é o próprio tabuleiro criado



#MÓDULO INTEGRANTE 1: tabuleiro
def criar_tabuleiro():
    """
    Cria o tabuleiro 8x8 e posiciona todas as peças nas posições iniciais
    
    Parâmetros: 
        bool

    Return: 
        tabuleiro
    """

    tabuleiro = [
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'], #linha 0 (pretas)
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'], #linha 1 (pretas)
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  #linha 2
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # linha 3
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # linha 4
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], # linha 5
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],  # linha 6 (brancas)
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']  # linha 7 (brancas)
    ]
    return tabuleiro


def mostrar_tabuleiro(tabuleiro): 
    """
    Organiza o tabuleiro, colocando as casas brancas e pretas vazias nas posições corretas do tabuleiro
    
    Parâmetros: 
        tabuleiro (lista)

    Return:
        bool
    """
    # organização das letras (acima) e dos números que representam as coordenadas do tabuleiro
    letras = ('a','b','c','d','e','f','g','h')
    print('    ' + '   '.join(letras))
    print('   ' + '-' * 33)
    numeros = ('8','7','6','5','4','3','2','1')

    for linha in range(8): #sequência de 0 a 7 pra representar a linha da matriz
        linha_sequencia = numeros[linha] + ' ' #1°) coloca a sequências dos números na esquerda

        for coluna in range(8): #sequência de 0 a 7 pra representar a coluna da matriz
            casa = tabuleiro[linha][coluna] #mostra o que está presente nos valores do tabuleiro

            if coluna == 0: 
                linha_sequencia += '| ' #2°) acrescenta | no começo para separar os números da primeira coluna

            if casa != " ": 
                linha_sequencia += casa #3°) acrescenta as peças na linha
                if coluna in range (8):
                    linha_sequencia += '  |' #4°) coloca | para representar uma divisória entre as peças
            else: #casas vazias
                if (linha + coluna) % 2 == 0: #5°) casas brancas: linha + coluna = par, ex: [2][4] = 6
                    linha_sequencia += '▓▓'
                else: #6°) casas pretas: a soma é ímpar
                    linha_sequencia += '░░' 

                if coluna in range (8): #acrescenta | para separar as colunas das casas brancas e pretas
                    linha_sequencia += ' |'#7°) coloca | para representar uma divisória entre as casas brancas e pretas
                
        linha_sequencia += ' ' + numeros[linha] #8°) coloca a sequências dos números na direita
        print(linha_sequencia)

    # organização das letras abaixo do tabuleiro
    print('   ' + '-' * 33)
    letras = ('a','b','c','d','e','f','g','h')
    print('    ' + '   '.join(letras))

    
def posicao_valida(linha_escolhida, coluna_escolhida):
    """
    Verifica se a posição que o jogador escolheu está dentro do limite da matriz 8x8
        
    Parâmetros:
        linha_escolhida
        coluna_escolhida
        
    Return:
        bool
    """
    if 0 <= linha_escolhida < 8 and 0 <= coluna_escolhida < 8:
        return True
    else:
        return False

def mover_peca(tabuleiro, origem, destino): 
    """
    Atualiza o tabuleiro após os movimentos das peças

    Parâmetros:
        tabuleiro
        origem
        destino
    
    Return:
        bool
    
    """
 
    linha_origem, coluna_origem = origem 
    linha_destino, coluna_destino = destino

    escolha = tabuleiro[linha_origem][coluna_origem] #lê a posição de origem da peça escolhida
    tabuleiro[linha_destino][coluna_destino] = escolha #coloca a peça na posição de destino
    tabuleiro[linha_origem][coluna_origem] = ' ' #esvazia a casa em que estava a peça antes

if __name__ == "__main__":
    main()