import sys
import pygame
from Nivel_Zelda import Nivel

class Zelda:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 550))
        pygame.display.set_caption("Zelda")
        self.nivel = Nivel()

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit()

            self.screen.fill("black")
            self.nivel.corre()
            pygame.display.update()

if __name__ == "__main__":
    zelda_juego = Zelda()
    zelda_juego.corre_juego()
