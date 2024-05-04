# Aqui será implementado o algoritmo MINMAX

# board - estado atual do jogo
# depth - representa a profundidade da recursão (quantos níveis da árvore de busca foram explorados)
# is_maximizing - um booleano que indica se o jogador atual está tentando maximizar sua pontuação

# A ideia é ter dois jogadores X (MAX) e O(MIN)

def minimax(board, depth, isMaximizing):
    # Verifica se o jogo terminou no estado atual do tabuleiro
    if checkWinner(board):
        # aqui precisa retornar a pontuação -- mais alta se o jogador estiver numa posição vantajosa -- mais baixa se o jogador estiver em desvantagem
        return getScore(board)

    # Se verdadeiro, significa que é a vez do jogador maximizador (geralmente representado por 'X' no jogo).
    if isMaximizing:
        # Inicializa a melhor pontuação para o MAX -- número bem altão
        best_score = -100000000000
        # Itera sobre todas as jogadas possíveis a partir do estado atual do tabuleiro.
        for move in getPossibleMoves(board):
            board[move] = 'X'  # faz jogada para o jogador MAX
            # Chama recursivamente a função minimax com o novo estado do tabuleiro após a jogada,
            # incrementa a profundidade e define is_maximizing como falso, pois agora é a vez do jogador minimizador.
            score = minimax(board, depth+1, False)
            # Desfaz a jogada para reverter o estado do tabuleiro
            board[move] = ' '
            # Atualiza a melhor pontuação encontrada até agora, escolhendo o máximo entre a pontuação atual e a melhor pontuação anterior.
            best_score = max(score, best_score)
        return best_score

    # Se o jogador atual não fizer a sua melhor jogada (não ta tentando maximizar sua pontuação)
    # significa que é a vez do jogador MIN.
    else:
        best_score = +10000000000
        for move in getPossibleMoves(board):
            board[move] = 'O'
            score = minimax(board, depth+1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score


def getScore():
    return null


def getPossibleMoves():
    return null


def checkWinner():
    return null
