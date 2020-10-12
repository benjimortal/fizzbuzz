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


def main():
    # Initialize pygame
    global mouse_x
    global bullet_state
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Title an Icon
    pygame.display.set_caption("Beyond Nowhere")
    icon = pygame.image.load("spaceship.png")
    pygame.display.set_icon(icon)

    #backgrund image
    #back_ground = pygame.image.load("background.jpg")
    #pygame.display.set_icon(back_ground)

    # Player
    player_Img = pygame.image.load("spaceship (2).png")
    position_x = 370
    position_y = 520

    position_x_change = 0
    position_y_change = 0

    # create bullet

    #ready- you can't see the bullet on the screen
    #fire- the bullet is currently moving
    bullet_Img = pygame.image.load("bullet.png")
    bullet_x = 0
    bullet_y = 480
    bullet_x_change = 0
    bullet_y_change = 10
    bullet_state = "ready"

    # Enemy
    enemy_Img = pygame.image.load("monster1.png")
    enemy_x = random.randint(0, 800)
    enemy_y = random.randint(50, 150)
    enemy_x_change = 4
    enemy_y_change = 10

    #Background

    background = pygame.image.load("background1.png")

    def player(x, y):
        screen.blit(player_Img, (round(x), round(y)))

    def enemy(x, y):
        screen.blit(enemy_Img, (round(x), round(y)))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bullet_Img, (x + 16, y + 10))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # if keystroke is pressed down check whether its right or left?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position_x_change -= 3
                if event.key == pygame.K_RIGHT:
                    position_x_change += 3
                if event.type == pygame.K_SPACE:
                    bullet_x = position_x
                    fire_bullet(bullet_x, bullet_y)

        position_x += position_x_change
        if position_x <= 0:
            position_x = 0
        elif position_x >= 736:
            position_x = 736

        enemy_x += enemy_x_change

        if enemy_x <= 1:
            enemy_x_change = 3
            enemy_y += enemy_y_change
        elif enemy_x >= 730:
            enemy_x_change = -3
            enemy_y += enemy_y_change

        #bullet movment
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state is "ready"

        if bullet_state is "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        screen.fill(ALICEBLUE)
        screen.blit(background, (0, 0))
        player(position_x, position_y)
        enemy(enemy_x, enemy_y)
        fire_bullet(position_x, bullet_y)
        pygame.display.update()


if __name__ == '__main__':
    main()
