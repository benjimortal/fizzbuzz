import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((245, 222, 179))
        pygame.display.update()


if __name__ == '__main__':
    main()
