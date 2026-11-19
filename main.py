def main ():
    """
    Cria as informações iniciais para começar o jogo e guarda as variáveis locais
    """
    print("=" * 11, "JOGO DE XADREZ", "=" * 11)
    print(" ")

    criado = criar_tabuleiro() #a variável está chamando a função que mostra o tabuleiro criado
    mostrar_tabuleiro(criado) #mostra a variável "criado" que é o próprio tabuleiro criado



#MÓDULO INTEGRANTE 1: tabuleiro
