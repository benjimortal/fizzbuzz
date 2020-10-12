import pygame


class Ball:
    def __init__(self, x, y, vel_x, vel_y, color, radius):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color
        self.radius = radius

    def collide(self, other_obj):
        my_rect = pygame.Rect((self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2))
        other_rect = pygame.Rect((self.x-self.radius, self.y-self.radius, self.radius * 2, self.radius * 2))
        return my_rect.collidedict(other_rect)


def main():
    pass


if __name__ == '__main__':
    main()
