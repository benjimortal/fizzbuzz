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
YELLOW = (255, 255, 0)

speed = 50


width = 800
height = 600
background = pygame.image.load("background.png")

icon = pygame.image.load("monster (7).png")
pygame.display.set_icon(icon)

class Player:
    def __init__(self, x, y, x_step, y_step, screen ):
        self.x = x
        self.y = y
        self.screen = screen
        self.x_step = x_step
        self.y_step = y_step


"""class Enemy:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),self.radius)

    def move(self):
        self.y += self.y_step

        if self.y >= 800:
            self.x = random.randrange(self.radius, 600-self.radius)
            self.y = - self.radius"""



def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("STAR WARS")
    player_img = pygame.image.load("monster (8).png")
    colors = [RED, GREEN, BLUE, SNOW, ALICEBLUE, LAVENDER, WHEAT, PINK]
    ball = Player(400, 550, -1, 1, random.choice(colors))

    """enemys = []
    for _ in range(1500):
        x = random.randrange(10, 800 - 20)
        y = random.randrange(10, 600 - 20)
        x_step = random.choice([ 1, 2, 3])
        y_step = random.choice([1, 2, 3])
        color = YELLOW  # random.choice(self.colors)
        radius = 1  # or just add radius = 20
        enemy = Enemy(x, y, x_step, y_step, color, radius,screen)
        enemys.append(enemy)"""

    keep_alive = True
    clock = pygame.time.Clock()
    while keep_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_alive = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ball.x - speed > 10:
            ball.x -= speed
        if keys[pygame.K_d] and ball.x + speed + 5 < width:
            ball.x += speed
        if keys[pygame.K_w] and ball.y - speed > 10:
            ball.y -= speed
        if keys[pygame.K_s] and ball.y + speed + 5 < height:
            ball.y += speed

        screen.blit(background, (0, 0))
        #for enemy in enemys:
         #   enemy.draw()
          #  enemy.move()
        screen.blit(player_img, [400, 520])

        pygame.display.update()
        clock.tick(90)

if __name__ == '__main__':
    main()
