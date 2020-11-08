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

animation_increment = 2
background_image = pygame.transform.scale(pygame.image.load(os.path.join("background.png")), (screen_width, screen_height))


class Ball:
    def __init__(self, x, y, x_step, y_step, color, screen, radius):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.screen = screen
        self.radius = radius

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)



def main():
    pygame.init()
    pygame.display.set_caption("The space between us")
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball = Ball(200, 500, -1, 1, RED, 20, screen)

    running = True
    clock = pygame.time.Clock()
    clock.tick(90)
    #background_image = pygame.image.load("space.jpg").convert()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.blit(background_image, [0, 0])
    ball.draw()
    ball.move()
    pygame.display.update()


if __name__ == '__main__':
    main()
