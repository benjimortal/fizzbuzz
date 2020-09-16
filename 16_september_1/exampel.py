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
    x = 400
    x_step = -2
    y = 300
    y_step = 2


    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (x, y), 10)

        pygame.display.update()
        y += y_step
        if y >= 590:
            y_step = -2
        if y <= 10:
            y_step = 2
            #or
            """y += y_step
            if not y <= 10 or y >= 590:
                y_step *= -1"""



        x += x_step
        if x >= 790:
            x_step = -2
        if x <= 10:
            x_step = 2


        """x += x_step
        if not x <= 10 or x <= 790:
            x_step *= -1"""

        clock.tick(FPS) #styr fatr, bildpunkter

if __name__ == '__main__':
    main()