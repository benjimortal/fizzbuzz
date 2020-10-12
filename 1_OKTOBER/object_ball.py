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
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 1)

    def collide(self, other):
        if self.left() >= other.right() or other.left() >= self.right():
            return False
        if self.top() >= other.bottom() or other.top() >= self.bottom():
            return False
        return True


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

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def show_next_hit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    blue_rect = Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100, BLUE, screen)

    colors = [WHITE, RED, GREEN, BLUE]

    balls = []
    for _ in range(10):
        x = random.randrange(10, SCREEN_WIDTH-20)
        y = random.randrange(10, SCREEN_HEIGHT-10)
        x_step = random.choice([-3, -2, -1, 0, 1, 2, 3])
        y_step = random.choice([-3, -2, -1, 0, 1, 2, 3])
        color = random.choice(colors)
        radius = random.randrange(5, 20) # or just add radius = 20
        ball = Ball(x, y, x_step, y_step, color, radius, screen)
        balls.append(ball)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            blue_rect.x = mouse_x
            blue_rect.y = mouse_y

        screen.fill(BLACK)
        for ball in balls:
            ball.move()
            ball.draw()
        blue_rect.draw()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()