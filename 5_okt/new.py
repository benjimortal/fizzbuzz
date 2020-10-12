import pygame

pygame.font.init()

screen_width = 800
screen_height = 600


class Ball:
    def __init__(self, x, y, x_step, y_step, radius, color, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if not self.radius <= self.x <= screen_width - self.radius:
            self.x_step *= -1
        if not self.radius <= self.y <= screen_height - self.radius:
            self.y_step *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True
    clock = pygame.time.Clock()
    ball = Ball(300, 200, -2, 1, 20, (0, 255, 0), screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        """if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ball.x = mouse_x
            ball.y = mouse_y
            pygame.mouse.set_visible(False)"""

        screen.fill((0, 0, 0))
        ball.draw()
        ball.move()

        pygame.display.flip()
        #pygame.display.update()
        clock.tick(190)

if __name__ == '__main__':
    main()
