import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    running = True
    x1 = 400
    x_step1 = -2
    y1 = 300
    y_step1 = 2

    x2 = 700
    x_step2 = 1
    y2 = 200
    y_step2 = -1
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (x1, y1), 10, 1)
        pygame.draw.circle(screen, GREEN, (x2, y2), 10, 1)

        pygame.display.update()
        y1 += y_step1

        if not 10 <= y1 <= 590:
            y_step1 *= -1

        x1 += x_step1
        if not 10 <= x1 <= 790:
            x_step1 *= -1

        y2 += y_step2

        if not 10 <= y2 <= 590:
            y_step2 *= -1

        x2 += x_step2
        if not 10 <= x2 <= 790:
            x_step2 *= -1

        clock.tick(FPS)

if __name__ == '__main__':
    main()