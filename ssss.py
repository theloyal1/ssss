import random

import pygame
from pygame.locals import *

def on_grid_random(): # Função para gerar uma posição aleatória na tela
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2): # Função para verificar se houve colisão entre a cobra e a maçã
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

"""
def fim_de_jogo(screen): # Função para exibir a mensagem de fim de jogo
    title_font = pygame.font.Font(None, 70)
    text_font = pygame.font.Font(None, 36)

    title = title_font.render("MORTO", True, (255, 0, 0))
    text = text_font.render("Pressione qualquer tecla para sair", True, (255, 255, 255))

    screen.fill((0, 0, 0))

    screen.blit(title, (250, 250))
    screen.blit(text, (250, 300))
    pygame.quit()
    exit()
"""
    
def reiniciar_jogo(): # Função para reiniciar o jogo
    global cobra, direcao, maca_pos
    cobra = [(200, 200), (210, 200), (220, 200)]
    direcao = LEFT
    maca_pos = on_grid_random()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((88, 230, 83))
pygame.display.set_caption("SSSSSSS")
fonte = pygame.font.Font(None, 36)

# Definindo a cobra e a maçã
cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pygame.Surface((10, 10))
cobra_skin.fill((0,0,255))

maca = pygame.Surface((10, 10))
maca.fill((255,0,0))
maca_pos = on_grid_random() # Posição aleatória da maçã

direcao = LEFT
pontuacao = 0

# Loop principal do jogo
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    # Verificando eventos do teclado
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT

    # Verificando colisão com a maçã
    if collision(cobra[0], maca_pos):
        maca_pos = on_grid_random()
        cobra.append((0,0))
        pontuacao += 1

    # Atualizando a posição da cobra
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    # Atualizando a posição da cabeça da cobra com base na direção
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    # Verificando colisão com as bordas da tela e consigo mesma
    if cobra[0][0] < 0 or cobra [0][0] >= 600 or cobra [0][1] <0 or cobra [0][1] >= 600 or cobra[0] in cobra[1:]:
        screen = pygame.display.set_mode((600, 600))
        pontuacao = 0
        reiniciar_jogo()

    # Verificando colisão com as bordas da tela
    screen.fill((88, 230, 83))
    screen.blit(maca, maca_pos)
    for pos in cobra:
        screen.blit(cobra_skin, pos)

    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    screen.blit(texto_pontuacao, (10, 10))

    pygame.display.update()