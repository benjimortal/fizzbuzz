import pygame
import random


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

class Ball:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen






    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True
    ball = Ball(370, 520, 1, -1, PINK, 20, screen )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill(WHEAT)
        ball.draw()
        ball.move()
        pygame.display.update()

if __name__ == '__main__':
    main()
