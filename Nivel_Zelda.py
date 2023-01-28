import pygame
import Mapa_Zelda
from Tiles_Zelda import Tile
from Link import Link


class Nivel:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.Sprites_deFondo = YGrupoCamara()
        self.Obtaculos = pygame.sprite.Group()

        self.crearMapa()

    def crearMapa(self):
        for row_index, row in enumerate(Mapa_Zelda.mapa):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 56
                if col == "x":
                    Tile((x,y), [self.Sprites_deFondo, self.Obtaculos])
                if col == "L":
                    self.Link = Link((x,y), [self.Sprites_deFondo], self.Obtaculos)

    def corre(self):
        self.Sprites_deFondo.dibuja(self.Link)
        self.Sprites_deFondo.update()


class YGrupoCamara(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def dibuja(self, Link):
        self.offset.x = Link.rect.centerx - self.half_width
        self.offset.y = Link.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_rect)
