import Tabuleiro.tabuleiro as t
import pygame
from InterfaceGrafica.config import *

pygame.init()

canvas = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Connect4")


# Centralizar os elementos
tamanho_quadrado = (TAMANHO_CIRCULO * 7) + (ESPACO_ENTRE_CIRCULOS * 6)
posicao_quadrado = ((LARGURA_TELA - tamanho_quadrado) // 2,
                    (ALTURA_TELA - tamanho_quadrado) // 2)


def desenhar_tabuleiro(matriz_tabuleiro):
    # Borda
    pygame.draw.rect(
      canvas, AZUL_CLARO, (posicao_quadrado[0] - 5, posicao_quadrado[1] - 5, tamanho_quadrado + 10, tamanho_quadrado + 10))
    # Quadrado azul
    pygame.draw.rect(
      canvas, AZUL, (posicao_quadrado[0], posicao_quadrado[1], tamanho_quadrado, tamanho_quadrado))

    # Desenhar círculos na matriz
    for linha in range(len(matriz_tabuleiro)):
      for coluna in range(len(matriz_tabuleiro[linha])):
        x = posicao_quadrado[0] + coluna * \
            (TAMANHO_CIRCULO + ESPACO_ENTRE_CIRCULOS) + TAMANHO_CIRCULO // 2
        y = posicao_quadrado[1] + tamanho_quadrado - (linha + 1) * \
           (TAMANHO_CIRCULO + ESPACO_ENTRE_CIRCULOS) + TAMANHO_CIRCULO // 2 + 10

        cor = PRETO

        if matriz_tabuleiro[linha][coluna] == 1:
          cor = AMARELO
        elif matriz_tabuleiro[linha][coluna] == 2:
            cor = VERMELHO

        pygame.draw.circle(canvas, cor, (x, y),
                            TAMANHO_CIRCULO // 2)
            

def connect_4(tabuleiro):
  exit = False

  matriz_tabuleiro = tabuleiro.grid

  while not exit:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit = True

      canvas.fill((255, 255, 255))
      desenhar_tabuleiro(matriz_tabuleiro)
      pygame.display.update()