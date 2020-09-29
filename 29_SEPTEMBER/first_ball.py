import pygame

# in i pygame position (0, 0) är högts upp på vänster sidan av skärmen, men i Turtle är (0,0) mitt på skärmen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 100


def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    running = True
    y = 300
    y_step = 2
    x = 400
    x_step = 2

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLUE)

        pygame.draw.circle(screen, RED, (x, y), 10)
        pygame.display.update()
        y += y_step
        if y <= 10 or y >= 590:#10 är radian på bollen
            y_step *= -1

        x += x_step
        if x <= 10 or x >= 790:
            x_step *= -1
        clock.tick(FPS)


if __name__ == '__main__':
    main()
