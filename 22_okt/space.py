import pygame
import random
screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load("background.png")
bullet = pygame.image.load("bullet.png")
spaceship = pygame.image.load("spaceship.png")
bullet_y = 500
fired = False


enemies = ["alien (4).png","alien (5).png"]
e_index = 0
enemy = pygame.image.load(enemies[e_index])
enemy_x = random.randint(50, 700)
move_direction = "right"
spaceship_x = True

keep_alive = "right"

clock = pygame.time.Clock()
while keep_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        fired = True

    if move_direction == "right":
        enemy_x += 50
    if enemy_x == 800:
        move_direction = "left"
    else:
        enemy_x -= 50
        if enemy_x == 0:
            move_direction = "right"

    if fired is True:
        bullet_y -= 5
    if bullet_y == 50:
        fired = False
        bullet_y = 500

    if bullet_y < 80 and 120 < enemy_x < 180:
        e_index += 1
        if e_index < len(enemies):
            enemy = pygame.image.load(enemies[e_index])
            enemy_x = 10

        else:
            print("YOU WIN")
            keep_alive = False

    screen.blit(background, [0, 0])
    screen.blit(enemy, [enemy_x, 50])
    screen.blit(bullet, [176, bullet_y])
    screen.blit(spaceship, [160, 500])
    pygame.display.update()
    clock.tick(90)

