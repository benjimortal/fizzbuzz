import pygame
import random

from object_ball2 import Rect

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAX_RADIUS = 40

class Ball:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1


        box_left = 350
        box_right = 450
        box_top = 250
        box_bottom = 350

        if box_left <= self.x <= box_right:
            if box_top <= self.y <= box_bottom:
                #we got a hit

                #left side?
                if box_left <= self.x <= box_left + self.radius:
                    self.x_step *= -1

                    #right side?
                if box_right <= self.x <= box_right - self.radius:
                    self.x_step *= -1



    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def show_next_hit(self):
        shaddow_x = self.x
        shaddow_y = self.y

        no_hit = True
        while no_hit:
            shaddow_x += self.x_step
            shaddow_y += self.y_step

            if not self.radius <= shaddow_x <= SCREEN_WIDTH - self.radius:
                no_hit = False

            if not self.radius <= shaddow_y <= SCREEN_HEIGHT - self.radius:
                no_hit = False

        pygame.draw.circle(self.screen, GREEN, (shaddow_x, shaddow_y), self.radius, 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ball = Ball(200, 500, -1, 1, RED, 20, screen)
    blue_rect = Rect(screen)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        ball.move()
        ball.draw()
        #ball.show_next_hit()
        pygame.draw.rect(screen, BLUE,(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100))
        pygame.display.update()
        clock.tick(2000)

if __name__ == '__main__':
    main()
