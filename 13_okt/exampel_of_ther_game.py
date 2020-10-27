import pygame
import random
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height)) #Creating screen
background = pygame.image.load("background.png") #Creating background

pygame.display.set_caption("Beyond the Nowhere...") #Creating caption
icon = pygame.image.load("monster.png")  #Creating Icon for screen
pygame.display.set_icon(icon)

player_img = pygame.image.load("spaceship.png") #Creating the player image
player_x_p = 370
player_y_p = 520

enemy_img = pygame.image.load("alien (4).png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)


class Player():
    def __init__(self, playerX, playerY, p_x_step, p_y_step):
        self.playerX = playerX
        self.playerY = playerY
        self.x_step = p_x_step
        self.y_step = p_y_step



class Enemy():
    def __init__(self, enemy_x, enemy_y, x_step, y_step):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.x_step = x_step
        self.y_step = y_step

    def move(self):
        self.enemy_x += self.x_step








def main():
    pygame.init()



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.blit(background, (0, 0))
        screen.blit(player_img, (player_x_p, player_y_p))
        pygame.display.update()



if __name__ == '__main__':
    main()
