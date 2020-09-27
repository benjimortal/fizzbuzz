import pygame

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

    def collide(self, other):
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

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def show_next_hit(self):
        shadow_x = self.x
        shadow_y = self.y

        no_hit = True
        while no_hit:
            shadow_x += self.x_step
            shadow_y += self.y_step

            if not self.radius <= shadow_x <= SCREEN_WIDTH - self.radius:
                no_hit = False

            if not self.radius <= shadow_y <= SCREEN_HEIGHT - self.radius:
                no_hit = False

        pygame.draw.circle(self.screen, GREEN, (shadow_x, shadow_y), self.radius, 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ball = Ball(200, 500, -1, 1, RED, 20, screen)
    blue_rect = Rect(SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2 - 50, 100, 100, BLUE, screen)
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
        ball.move()
        ball.draw()
        if blue_rect.collide(ball):
            if blue_rect.left <= ball.right <= blue_rect.left + 10:
                ball.x_step = -1
            if blue_rect.right >= ball.left >= blue_rect.right - 10:
                ball.x_step = 1
            if blue_rect.top <= ball.bottom <= blue_rect.top + 10:
                ball.y_step = -1
            if blue_rect.bottom >= ball.top >= blue_rect.bottom - 10:
                ball.y_step = 1


        # ball.show_next_hit()
        #pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2 - 50, 100, 100))
        blue_rect.draw()
        pygame.display.update()
        clock.tick(120)

if __name__ == '__main__':
    main()