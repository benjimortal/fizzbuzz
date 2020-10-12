import pygame

x = 800
y = 400


def get_image():
    image = pygame.image.load("ball2.png")


def main():
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    clock = pygame.time.Clock()

    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0, 0, 0))
        screen.blit(get_image("ball2.jpg"), (20, 20))
        pygame.display.flip()
        clock.tick(90)


if __name__ == '__main__':
    main()
