import pygame
import Mapa_Zelda

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("roca 2.1.png")
        self.rect = self.image.get_rect(topleft = pos)