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
    y1 = 290
    y_step1 = -2
    x1 = 390
    x_step1 = 2

    y2 = 390
    y_step2 = -2
    x2 = 490
    x_step2 = -1

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLUE)

        pygame.draw.circle(screen, RED, (x1, y1), 10)
        pygame.draw.circle(screen, GREEN, (x2, y2), 10, 1) # 2 är som visar kökleken på randen och vissar tom innuti

        pygame.display.update()
        y1 += y_step1
        if y1 <= 10 or y1 >= 590:#10 är radian på bollen
            y_step1 *= -1

        x1 += x_step1
        if x1 <= 10 or x1 >= 790:
            x_step1 *= -1

        y2 += y_step2
        if y2 <= 10 or y2 >= 590:  # 10 är radian på bollen
            y_step2 *= -1

        x2 += x_step2
        if x2 <= 10 or x2 >= 790:
            x_step2 *= -1

        clock.tick(FPS)




if __name__ == '__main__':
    main()
