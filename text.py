import pygame

# Inicializa o Pygame
pygame.init()

# Tamanho da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo com Sprite")

# Cores
BRANCO = (255, 255, 255)

# FPS
clock = pygame.time.Clock()
fps = 60

# Carregando uma imagem como sprite
sprite_img = pygame.image.load("personagem_1.png")
sprite_rect = sprite_img.get_rect()
sprite_rect.topleft = (100, 100)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação com teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        sprite_rect.x -= 5
    if teclas[pygame.K_RIGHT]:
        sprite_rect.x += 5
    if teclas[pygame.K_UP]:
        sprite_rect.y -= 5
    if teclas[pygame.K_DOWN]:
        sprite_rect.y += 5

    # Atualiza a tela
    tela.fill(BRANCO)
    tela.blit(sprite_img, sprite_rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
