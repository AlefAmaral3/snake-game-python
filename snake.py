import pygame, random

# Inicializa o pygame
pygame.init()

# ---------------------- CONFIGURAÇÕES BÁSICAS ----------------------
WIDTH, HEIGHT = 600, 400   # tamanho da janela
BLOCK = 20                 # tamanho de cada bloquinho da cobra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha 🐍")

# Cores (RGB)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonte para texto
font = pygame.font.SysFont(None, 32)

# ---------------------- VARIÁVEL DE RECORD ----------------------
high_score = 0  # armazena o recorde atual

# ---------------------- FUNÇÃO PARA DESENHAR TEXTO ----------------------
def draw_text(text, y):
    """Desenha texto centralizado na tela"""
    surf = font.render(text, True, WHITE)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)

# ---------------------- LOOP PRINCIPAL DO JOGO ----------------------
def game_loop():
    global high_score  # para poder alterar a variável global

    clock = pygame.time.Clock()
    snake = [(100, 100), (80, 100), (60, 100)]  # posição inicial da cobra
    direction = (BLOCK, 0)                      # começa indo pra direita
    food = (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))
    score = 0
    running = True

    while running:
        # ---------------------- CAPTURA EVENTOS ----------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK):
                    direction = (0, -BLOCK)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                    direction = (0, BLOCK)
                elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                    direction = (-BLOCK, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                    direction = (BLOCK, 0)

        # ---------------------- MOVIMENTO ----------------------
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # ---------------------- COMER COMIDA ----------------------
        if snake[0] == food:
            score += 1
            # Atualiza o recorde se necessário
            if score > high_score:
                high_score = score
            # Gera nova comida
            while True:
                food = (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))
                if food not in snake:
                    break
        else:
            snake.pop()  # remove o último pedaço se não comer

        # ---------------------- COLISÕES ----------------------
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            len(snake) != len(set(snake))):
            # se bater nas bordas ou em si mesma
            game_over(score)
            return

        # ---------------------- DESENHA TUDO NA TELA ----------------------
        screen.fill(BLACK)

        # Escolhe cor conforme o score
        if score < 5:
            color = (0, 255, 0)        # verde
        elif score < 10:
            color = (255, 255, 0)      # amarelo
        elif score < 20:
            color = (255, 165, 0)      # laranja
        else:
            color = (255, 0, 0)        # vermelho

        for segment in snake:
            pygame.draw.rect(screen, color, (*segment, BLOCK, BLOCK))


        pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

        # Mostra o score e o recorde
        draw_text(f"Score: {score}  |  Recorde: {high_score}", 20)

        pygame.display.flip()
        clock.tick(10)

# ---------------------- TELA DE GAME OVER ----------------------
def game_over(score):
    clock = pygame.time.Clock()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
        screen.fill((20, 20, 20))
        draw_text("💀 GAME OVER 💀", HEIGHT // 2 - 30)
        draw_text(f"Sua pontuação: {score}", HEIGHT // 2 + 10)
        draw_text("Pressione qualquer tecla para jogar novamente", HEIGHT - 40)
        pygame.display.flip()
        speed = 10 + (score // 3)
        clock.tick(speed)


# ---------------------- EXECUTA O JOGO ----------------------
while True:
    game_loop()