# Importa as bibliotecas necessárias
import pygame       # Biblioteca para jogos
import time         # Biblioteca para controlar o tempo (não está sendo usada aqui, mas pode ser útil)
import random       # Para gerar posições aleatórias da comida


# Inicializa todos os módulos do pygame
pygame.init()


# Definição de cores em formato RGB
branco = (255, 255, 255)    # Cor branca
vermelho = (213, 50, 80)    # Cor vermelha (mensagens de fim de jogo)
preto = (0, 0, 0)           # Cor preta (cor da cobrinha)
azul = (255, 255, 255)       # Cor de fundo da tela
verde = (213, 50, 80)         # Cor da comida

# Define as dimensões da janela do jogo
largura = 800
altura = 400

# Cria a janela com essas dimensões
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela
pygame.display.set_caption('Jogo da Cobrinha')

# Define o tamanho de cada "bloco" da cobra (pixels)
tamanho_bloco = 20

# Define a velocidade de atualização da tela (FPS)
velocidade = 10

# Define a fonte e tamanho do texto usado nas mensagens
fonte = pygame.font.SysFont("bahnschrift", 20)

# Cria um relógio para controlar o tempo de jogo
relogio = pygame.time.Clock()

# Função que exibe uma mensagem na tela (ex: fim de jogo)
def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)  # Renderiza o texto com a cor desejada
    tela.blit(texto, [largura / 6, altura / 3])  # Posiciona o texto na tela

# Função para desenhar a cobrinha na tela
def desenhar_cobra(bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], bloco, bloco])  # Desenha cada parte da cobra

# Função principal do jogo
def jogo():
    fim_jogo = False         # Controla quando o jogo deve encerrar
    game_over = False        # Controla quando o jogador perde

    # Posição inicial da cobra (centro da tela)
    x = largura / 2
    y = altura / 2

    # Mudança inicial de direção (parado)
    x_mudanca = 0
    y_mudanca = 0

    # Lista que guarda as posições da cobra
    lista_cobra = []
    comprimento_cobra = 1    # Começa com 1 bloco

    # Gera a posição da comida aleatoriamente na tela
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    # Loop principal do jogo
    while not fim_jogo:

        # Loop de fim de jogo (quando o jogador perde)
        while game_over:
            tela.fill(branco)  # Preenche a tela de branco
            mensagem("Você perdeu! Pressione C para continuar ou Q para sair", vermelho)
            pygame.display.update()  # Atualiza a tela com a mensagem

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Se o jogador apertar uma tecla
                    if event.key == pygame.K_q:   # Sair do jogo
                        fim_jogo = True
                        game_over = False
                    if event.key == pygame.K_c:   # Reiniciar o jogo
                        jogo()

        # Loop de eventos do pygame (movimentação, fechar janela, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True  # Fecha o jogo se clicar no X da janela
            if event.type == pygame.KEYDOWN:
                # Define a direção da cobra com as teclas do teclado
                if event.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Atualiza a posição da cabeça da cobra
        x += x_mudanca
        y += y_mudanca

        # Se sair da tela, perde o jogo
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True

        # Preenche o fundo da tela
        tela.fill(azul)
        # Desenha a comida na tela
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualiza a posição da cabeça da cobra
        cabeca_cobra = [x, y]
        lista_cobra.append(cabeca_cobra)  # Adiciona a nova posição à lista

        # Se o tamanho da lista for maior que o comprimento, remove o último
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica se a cobra bateu em si mesma
        for parte in lista_cobra[:-1]:
            if parte == cabeca_cobra:
                game_over = True

        # Desenha a cobra com base na lista de posições
        desenhar_cobra(tamanho_bloco, lista_cobra)

        # Atualiza a tela
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1  # Aumenta o tamanho da cobra

        # Controla a velocidade do jogo
        relogio.tick(velocidade)

    # Encerra o pygame e o programa
    pygame.quit()
    quit()

# Inicia o jogo chamando a função principal
jogo()
