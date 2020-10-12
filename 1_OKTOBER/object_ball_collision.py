import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Rect:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color
        self.screen = screen


    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 3)

    def collide(self, other):
        if self.left() >= other.right() or other.left() >= self.right():
            return False
        if self.top() >= other.bottom() or other.top() >= self.bottom():
            return False
        return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    red_rect = Rect(200, 200, 50, 50, RED, screen)
    blue_rect = Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100, BLUE, screen)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    red_rect.x -= 10
                if event.key == pygame.K_RIGHT:
                    red_rect.x += 10
                if event.key == pygame.K_UP:
                    red_rect.y -= 10
                if event.key == pygame.K_DOWN:
                    red_rect.y += 10


        screen.fill(BLACK)
        red_rect.draw()
        blue_rect.draw()
        if red_rect.collide(blue_rect):
            print("HIIIIIIT")
        else:
            print("NOOOOO HIIIIIT")
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
