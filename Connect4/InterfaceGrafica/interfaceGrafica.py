import pygame
from config import *

pygame.init()

canvas = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
exit = False
pygame.display.set_caption("Connect4")

# Inicializa a matriz com todos os círculos pretos
matriz_circulos = [['Preto'] * 7 for _ in range(7)]

# Centralizar os elementos
tamanho_quadrado = (TAMANHO_CIRCULO * 7) + (ESPACO_ENTRE_CIRCULOS * 6)
posicao_quadrado = ((LARGURA_TELA - tamanho_quadrado) // 2,
                    (ALTURA_TELA - tamanho_quadrado) // 2)


def desenhar_quadrado():
    # Borda
    pygame.draw.rect(
        canvas, AZUL_CLARO, (posicao_quadrado[0] - 5, posicao_quadrado[1] - 5, tamanho_quadrado + 10, tamanho_quadrado + 10))
    # Quadrado azul
    pygame.draw.rect(
        canvas, AZUL, (posicao_quadrado[0], posicao_quadrado[1], tamanho_quadrado, tamanho_quadrado))

    # Desenhar círculos na matriz
    for linha in range(7):
        for coluna in range(7):
            x = posicao_quadrado[0] + coluna * \
                (TAMANHO_CIRCULO + ESPACO_ENTRE_CIRCULOS) + TAMANHO_CIRCULO // 2
            y = posicao_quadrado[1] + linha * \
                (TAMANHO_CIRCULO + ESPACO_ENTRE_CIRCULOS) + TAMANHO_CIRCULO // 2
            if matriz_circulos[linha][coluna] == 'Preto':
                pygame.draw.circle(canvas, PRETO, (x, y),
                                   TAMANHO_CIRCULO // 2)


while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    canvas.fill((255, 255, 255))
    desenhar_quadrado()
    pygame.display.update()
