import pygame

TAMANHO_TELA = [600, 600]
TELA = pygame.display.set_mode(TAMANHO_TELA) # Gera tela

# Variaveis
vitoria = -1 # -1 = Ninguem; 0 = JOGADOR1; 1 = JOGADOR2; 2 = VELHA
semSombra = False
quantidadeGrid = 3

