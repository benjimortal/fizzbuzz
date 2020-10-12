import pygame
import os


white = (255, 255, 255)
black = (0, 0, 0)
RED = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

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

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        """if self.x < 0 + self.radius:
            self.x_step = 1
        if self.x > screen_width - self.radius:
            self.x_step = -1
        if self.y < 0 + self.radius:
            self.y_step = 1
        if self.y > screen_height - self.radius:
            self.y_step = -1"""
        if not self.radius <= self.x <= screen_width - self.radius:
            self.x_step *= -1
        if not self.radius <= self.y <= screen_height - self.radius:
            self.y_step *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True
    ball = Ball(400, 300, -1, 1, RED, 20, screen)

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                ball.x = mouse_x
                ball.y = mouse_y
                pygame.mouse.set_visible(False)

        screen.fill((0, 0, 0))
        ball.draw()
        ball.move()
        clock.tick(190)
        pygame.display.update()


if __name__ == '__main__':
    main()
