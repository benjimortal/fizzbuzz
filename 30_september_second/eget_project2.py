import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Rect:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color
        self.screen = screen

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 3)

    def collied(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
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

    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    @property
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if self.x < 0 + self.radius:
            self.x_step = 1
        if self.x > 800 - self.radius:
            self.x_step = -1
        if self.y < 0 + self.radius:
            self.y_step = 1
        if self.y > 600 - self.radius:
            self.y_step = -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    running = True

    ball = Ball(400, 300, -1, 1, GREEN, 20)
    clock = pygame.time.Clock()
    box = pygame.Rect(200, 200, 100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.draw.rect(screen, BLUE, box)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box.x -= 1
        if keys[pygame.K_RIGHT]:
            box.x += 1
        if keys[pygame.K_UP]:
            box.y -= 1
        if keys[pygame.K_DOWN]:
            box.y += 1

        screen.fill(BLACK)
        ball.move()
        ball.draw(screen)
        pygame.display.update()
        clock.tick(120)


if __name__ == '__main__':
    main()
