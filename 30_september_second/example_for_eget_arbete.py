
import pygame


pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

width = 800
height = 600

pixel = 64

pygame.display.set_caption("CRONA KILLER")
speed = 5



class Ball:
    def __init__(self, x, y, x_step, y_step, color, radius):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius



    def move(self):
        self.x += self.x_step


        if self.x < 0 + self.radius:
            self.x_step = 1
        if self.x > width - self.radius:
            self.x_step = -1
        if self.y < 0 + self.radius:
            self.y_step = 1
        if self.y > height - self.radius:
            self.y_step = -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)





def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    running = True

    ball = Ball(370, 520, -1, 1, (255, 0, 0), 20)
    clock = pygame.time.Clock()
    box = pygame.Rect(400, 400, 100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        ball.move()
        ball.draw(screen)
        pygame.draw.rect(screen, (0, 0, 255), box)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and box.x - speed > 0:
            box.x -= speed
        if keys[pygame.K_d]and box.x + speed +100 < width:
            box.x += speed
        if keys[pygame.K_w]and box.y - speed > 0:
            box.y -= speed
        if keys[pygame.K_s]and box.y + speed +100 < height:
            box.y += speed
        pygame.display.update()
        clock.tick(120)




if __name__ == '__main__':
    main()

