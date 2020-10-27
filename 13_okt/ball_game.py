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


ball = pygame.display.set_mode((screen_width,screen_height))
x = 370
y = 520
pygame.display.set_caption("Beyond the Nowhere...")


class Enemy:
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

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),self.radius)





def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    colors = [RED, GREEN, BLUE, SNOW, ALICEBLUE, LAVENDER, WHEAT, PINK]
    enemy  = Enemy(200, 500, -1, 1, RED, 20, screen)


    enemys = []
    for _ in range(20):
        x = random.randint(0, 800)
        y = random.randint(-1, 0)
        x_step = random.randint(10, 780)
        y_step = random.randint(-1, 610)
        color = random.choice(colors)
        radius = 20
        enemy = Enemy(x, y, x_step, y_step, color, radius, screen)
        enemys.append(enemy)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for enemy in enemys:
            enemy.draw()
            enemy.move()

        screen.fill(WHEAT)
        ball.draw()
        pygame.display.update()
if __name__ == '__main__':
    main()
