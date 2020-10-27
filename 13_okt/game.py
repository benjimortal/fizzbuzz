import pygame

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))   # Create a screen
background = pygame.image.load("background.png")   # Create a background

# Title and Icon
pygame.display.set_caption("Beyond the Nowhere...")
icon = pygame.image.load("monster.png")
pygame.display.set_icon(icon)


player_img = pygame.image.load("spaceship.png")   #Creating the player image
player_x = 370
player_y = 520
#player_x_position = 5


def player(x, y):
    screen.blit(player_img, (x, y))  # Drawing an image of our player on screen


def main():
    pygame.init()


    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        player(player_x, player_y)
        pygame.display.update()



if __name__ == '__main__':
    main()
