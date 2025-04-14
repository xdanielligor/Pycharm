import pygame
import random

# Inicialização do Pygame
pygame.init()

# Tamanho da tela
LARGURA = 800
ALTURA = 300
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Dinossauro")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Relógio
clock = pygame.time.Clock()
FPS = 30

# Dinossauro
dino_largura = 50
dino_altura = 50
dino_x = 50
dino_y = ALTURA - dino_altura - 20
dino_pulando = False
velocidade_pulo = 10
gravidade = 1

# Obstáculo
obst_largura = 20
obst_altura = 40
obst_x = LARGURA
obst_y = ALTURA - obst_altura - 20
velocidade_obstaculo = 10

# Pontuação
pontos = 0

# Função para desenhar o dinossauro
def desenhar_dino(x, y):
    pygame.draw.rect(TELA, VERDE, [x, y, dino_largura, dino_altura])

# Função para desenhar o obstáculo
def desenhar_obstaculo(x, y):
    pygame.draw.rect(TELA, PRETO, [x, y, obst_largura, obst_altura])

# Função para mostrar pontuação
def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    TELA.blit(texto, (10, 10))

# Função para detectar colisão
def colisao(rect1, rect2):
    return rect1.colliderect(rect2)

# Loop principal
rodando = True
pulo_vel = 0

while rodando:
    TELA.fill(BRANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Pulo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE] and not dino_pulando:
        dino_pulando = True
        pulo_vel = -velocidade_pulo

    if dino_pulando:
        dino_y += pulo_vel
        pulo_vel += gravidade
        if dino_y >= ALTURA - dino_altura - 20:
            dino_y = ALTURA - dino_altura - 20
            dino_pulando = False

    # Movimento do obstáculo
    obst_x -= velocidade_obstaculo
    if obst_x < -obst_largura:
        obst_x = LARGURA + random.randint(200, 600)
        pontos += 1

    # Colisão
    dino_rect = pygame.Rect(dino_x, dino_y, dino_largura, dino_altura)
    obst_rect = pygame.Rect(obst_x, obst_y, obst_largura, obst_altura)

    if colisao(dino_rect, obst_rect):
        texto = fonte.render("Game Over!", True, (255, 0, 0))
        TELA.blit(texto, (LARGURA // 2 - 80, ALTURA // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        rodando = False

    # Desenhar tudo
    desenhar_dino(dino_x, dino_y)
    desenhar_obstaculo(obst_x, obst_y)
    mostrar_pontos(pontos)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()