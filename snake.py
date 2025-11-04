import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha 🐍")

# Cores
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Função principal
def main():
    clock = pygame.time.Clock()
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = (BLOCK_SIZE, 0)
    food = (random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        # Move a cobra
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Comer a comida
        if snake[0] == food:
            food = (random.randrange(0, WIDTH, BLOCK_SIZE),
                    random.randrange(0, HEIGHT, BLOCK_SIZE))
        else:
            snake.pop()

        # Colisão com parede ou corpo
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            len(snake) != len(set(snake))):
            pygame.quit()
            sys.exit()

        # Desenhar
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
