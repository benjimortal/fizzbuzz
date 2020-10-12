import pygame
import os


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHEAT = (245, 222, 179)
LAVENDER = (230, 230, 250)
ALICEBLUE = (240, 248, 255)
SNOW = (255, 250, 250)


screen_width = 800
screen_height = 600


def main():
    pygame.init()
    window = pygame.display.set_mode((screen_width, screen_height))
    # creat a caption
    pygame.display.set_caption("Beyond Nowhere")
    #creat a icon
    icon = pygame.image.load("monster1.png")
    pygame.display.set_icon(icon)
    #creat a background
    background = pygame.image.load("background1.png")

    running = True
    clock = pygame.time.Clock()
    clock.tick(90)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window.blit(background)
            pygame.display.update()
if __name__ == '__main__':
    main()
