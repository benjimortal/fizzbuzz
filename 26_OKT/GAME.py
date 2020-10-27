import pygame
import os
import time
import random
pygame.font.init()


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHEAT = (245, 222, 179)
LAVENDER = (230, 230, 250)
ALICEBLUE = (240, 248, 255)
SNOW = (255, 250, 250)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, SNOW, ALICEBLUE, LAVENDER, WHEAT, PINK]

screen_width = 800
screen_height = 600
#Load images
enemy_1 = pygame.image.load(os.path.join("bilder 32.px", "1.png"))
enemy_2 = pygame.image.load(os.path.join("bilder 32.px", "2.png"))
enemy_3 = pygame.image.load(os.path.join("bilder 32.px", "3.png"))
enemy_4 = pygame.image.load(os.path.join("bilder 32.px", "4.png"))
enemy_5 = pygame.image.load(os.path.join("bilder 32.px", "5.png"))

#load player's_img
player_img = pygame.image.load("start-up.png")

#load background
background = pygame.image.load("background.png")

#change the icon
icon = pygame.image.load("spaceship (3).png")
pygame.display.set_icon(icon)

#bullet
bullet = pygame.image.load("bullet (4).png")

pygame.display.set_caption("STARS ABOVE US!!!!")

FPS = 60
level = 1
lives = 5
player_speed = 2
main_font = pygame.font.SysFont("Arial", 50)

lives_label = main_font.render(f"Lives: {lives}", 1, (YELLOW))
levels_label = main_font.render(f"Level: {level}", 1, (YELLOW))





class Spaceship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health



    def draw(self, screen):
        screen.blit(self.ship_img, (self.x, self.y))

class Player(Spaceship):
    def __init__(self, x, y, health = 100):
        super(). __init__(x, y , health)
        self.ship_img = player_img
        self.laser_img = bullet
        self.mask = pygame.mask.from_surface(self.ship_img)  #mask is pixel perfet collision
        self.max_health = health



class Enemy:
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

        if self.y >= screen_height:
            self.x = random.randrange(self.radius, screen_width - self.radius)
            self.y = -self.radius




def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    player = Player(400, 500)

    enemys = []
    for _ in range(10):
        x = random.randrange(10, screen_width - 20)
        y = random.randrange(10, screen_height - 20)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([ 1, 2, 3])
        color = random.choice(colors)
        radius = 20  # or just add radius = 20
        enemy = Enemy(x, y, x_step, y_step, color, radius, screen)
        enemys.append(enemy)



    keep_alive = True
    while keep_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_alive = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_speed >= -5:
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + 55 < screen_width:
            player.x += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0:
            player.y -= player_speed
        if keys[pygame.K_s] and player.y + player_speed + 65 < screen_height:
            player.y += player_speed


        screen.blit(background, (0,0))
        for enemy in enemys:
            enemy.draw()
            enemy.move()
        player.draw(screen)

        screen.blit(lives_label, (10,10))
        screen.blit(levels_label, (screen_width - levels_label.get_width ()- 10, 10))
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()
