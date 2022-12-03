import pygame
import Mapa_Zelda
from Tiles_Zelda import Tile
from Link import Link


class Nivel:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.Sprites_deFondo = pygame.sprite.Group()
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
                    Link((x,y), [self.Sprites_deFondo], self.Obtaculos)

    def corre(self):
        self.Sprites_deFondo.draw(self.screen)
        self.Sprites_deFondo.update()
