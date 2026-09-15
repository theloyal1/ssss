import random

import pygame
from pygame.locals import *

def on_grid_random(): # Função para gerar uma posição aleatória na tela
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2): # Função para verificar se houve colisão entre a cobra e a maçã
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
  
def reiniciar_jogo(): # Função para reiniciar o jogo
    global cobra, direcao, maca_pos
    cobra = [(200, 200), (210, 200), (220, 200)]
    direcao = LEFT
    maca_pos = on_grid_random()

def fim_de_jogo():
    screen.fill((54, 12, 12))

    titulo = pygame.font.Font(None, 80)
    texto = pygame.font.Font(None, 36)

    texto_titulo = titulo.render("FIM DE JOGO", True, (255, 0, 0))
    texto_pontuacao = texto.render(f"Pontuação final: {pontuacao}", True, (255, 255, 255))
    texto_reiniciar = texto.render("ENTER - Jogar novamente", True, (255, 255, 255))
    texto_sair = texto.render("ESC - Sair", True, (255, 255, 255))

    titulo_rect = texto_titulo.get_rect(center=(300, 200))
    screen.blit(texto_titulo, titulo_rect)
    pontuacao_rect = texto_pontuacao.get_rect(center=(300, 340))
    screen.blit(texto_pontuacao, pontuacao_rect)
    reiniciar_rect = texto_reiniciar.get_rect(center=(300, 380))
    screen.blit(texto_reiniciar, reiniciar_rect)
    sair_rect = texto_sair.get_rect(center=(300, 420))
    screen.blit(texto_sair, sair_rect)

    pygame.display.update()

def iniciar_jogo():
    screen.fill((27, 27, 27))

    titulo = pygame.font.Font(None, 80)
    opcoes = pygame.font.Font(None, 36)

    texto_titulo = titulo.render("SSSSSSS", True, (0, 124, 190))
    texto_jogar = opcoes.render("ENTER - Jogar", True, (255, 255, 255))
    texto_instrucoes = opcoes.render("I - Instruções", True, (255, 255, 255))
    texto_sair = opcoes.render("ESC - Sair", True, (255, 255, 255))

    titulo_rect = texto_titulo.get_rect(center=(300, 200))
    screen.blit(texto_titulo, titulo_rect)

    jogar_rect = texto_jogar.get_rect(center=(300, 340))
    instrucoes_rect = texto_instrucoes.get_rect(center=(300, 380))
    sair_rect = texto_sair.get_rect(center=(300, 420))

    screen.blit(texto_jogar, jogar_rect)
    screen.blit(texto_instrucoes, instrucoes_rect)
    screen.blit(texto_sair, sair_rect)

    pygame.display.update()

def instrucoes():
    screen.fill((27, 27, 27))

    titulo = pygame.font.Font(None, 64)
    secao = pygame.font.Font(None, 40)
    texto = pygame.font.Font(None, 30)

    texto_titulo = titulo.render("INSTRUÇÕES", True, (0, 124, 190))
    texto_controles = secao.render("CONTROLES", True, (255, 255, 255))
    texto_movimento = texto.render("Use as setas para mover a cobra.", True, (255, 255, 255))
    texto_objetivo = secao.render("OBJETIVO", True, (255, 255, 255))
    texto_macas = texto.render("Coma as maçãs para crescer e ganhar pontos.", True, (255, 255, 255))
    texto_velocidade = texto.render("A cada 5 maçãs comidas, a velocidade aumenta.", True, (255, 255, 255))
    texto_perigo = secao.render("PERIGO", True, (255, 255, 255))
    texto_gameover = texto.render("Evite bater na parede ou na própria cobra.", True, (255, 255, 255))
    texto_voltar = texto.render("ESC - Voltar", True, (255, 255, 255))

    titulo_rect = texto_titulo.get_rect(center=(300, 60))
    screen.blit(texto_titulo, titulo_rect)
    controles_rect = texto_controles.get_rect(topleft=(30, 135))
    screen.blit(texto_controles, controles_rect)
    movimento_rect = texto_movimento.get_rect(topleft=(30, 180))
    screen.blit(texto_movimento, movimento_rect)
    objetivo_rect = texto_objetivo.get_rect(topleft=(30, 220))
    screen.blit(texto_objetivo, objetivo_rect)
    macas_rect = texto_macas.get_rect(topleft=(30, 260))
    screen.blit(texto_macas, macas_rect)
    velocidade_rect = texto_velocidade.get_rect(topleft=(30, 300))
    screen.blit(texto_velocidade, velocidade_rect)
    perigo_rect = texto_perigo.get_rect(topleft=(30, 340))
    screen.blit(texto_perigo, perigo_rect)
    gameover_rect = texto_gameover.get_rect(topleft=(30, 380))
    screen.blit(texto_gameover, gameover_rect)
    voltar_rect = texto_voltar.get_rect(center=(300, 420))
    screen.blit(texto_voltar, voltar_rect)

    pygame.display.update()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

estado = "inicio"  # Estado inicial do jogo

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((27, 27, 27))
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
velocidade = 15
high_score = 0

# Loop principal do jogo
clock = pygame.time.Clock()

while True:
    clock.tick(velocidade)
    # Verificando eventos do teclado
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if estado == "inicio":
                if event.key == K_RETURN:
                    reiniciar_jogo()
                    pontuacao = 0
                    velocidade = 15
                    estado = "jogando"

                elif event.key == K_i:
                    estado = "instrucoes"

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

            if estado == "instrucoes":
                if event.key == K_ESCAPE:
                    estado = "inicio"

            if estado == "game_over":
                if event.key == K_RETURN:
                    reiniciar_jogo()
                    pontuacao = 0
                    velocidade = 15
                    estado = "jogando"
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
        
            elif estado == "jogando":
                if event.key == K_UP and direcao != DOWN:
                    direcao = UP
                if event.key == K_DOWN and direcao != UP:
                    direcao = DOWN
                if event.key == K_RIGHT and direcao != LEFT:
                    direcao = RIGHT
                if event.key == K_LEFT and direcao != RIGHT:
                    direcao = LEFT

    if estado == "jogando":
        # Verificando colisão com a maçã
        if collision(cobra[0], maca_pos):
            maca_pos = on_grid_random()
            cobra.append((0,0))
            pontuacao += 1

            if pontuacao > high_score:
                high_score = pontuacao

            if pontuacao % 5 == 0 and velocidade < 31:
                velocidade += 2

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
            estado = "game_over"

    if estado == "inicio":
        iniciar_jogo()
    elif estado == "instrucoes":
        instrucoes()
    elif estado == "jogando":
        # Verificando colisão com as bordas da tela
        screen.fill((88, 230, 83))
        screen.blit(maca, maca_pos)
        for pos in cobra:
            screen.blit(cobra_skin, pos)

        fonte_jogando = pygame.font.Font(None, 30)
        texto_pontuacao = fonte_jogando.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
        texto_velocidade = fonte_jogando.render(f"Velocidade: {velocidade}", True, (255, 255, 255))
        texto_maior_pontuacao = fonte_jogando.render(f"Recorde: {high_score}", True, (255, 255, 255))
        pontuacao_rect = texto_pontuacao.get_rect(topleft=(10, 10))
        velocidade_rect = texto_velocidade.get_rect(center=(300, 20))
        maior_pont_rect = texto_maior_pontuacao.get_rect(topright=(590, 10))
        screen.blit(texto_pontuacao, pontuacao_rect)
        screen.blit(texto_velocidade, velocidade_rect)
        screen.blit(texto_maior_pontuacao, maior_pont_rect)

        pygame.display.update()
    elif estado == "game_over":
        fim_de_jogo()