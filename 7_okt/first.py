import pygame
import os

width = 800
height = 700
animation_increment = 2
background_image = pygame.transform.scale(pygame.image.load(os.path.join("space.jpg")), (width, height))



class Ball:
    def __init__(self, x, y, x_step, y_step, screen):
        self.x = x
        self.y = y
        self.ball_img = None
        self.x_step = x_step
        self.y_step = y_step
        self.screen = screen

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

    def draw(self):
        pygame.draw(self.screen, (self.x, self.y))



def main():
    pygame.init()
    size = (width, height)
    pygame.display.set_caption("The space between us")
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()
    clock.tick(90)
    #background_image = pygame.image.load("space.jpg").convert()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, [0, 0])
        pygame.display.update()


if __name__ == '__main__':
    main()
