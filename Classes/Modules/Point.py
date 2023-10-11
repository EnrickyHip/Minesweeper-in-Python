import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super(pygame.sprite.Sprite, self).__init__()
        self.rect = pygame.Rect(x, y, 1, 1)
