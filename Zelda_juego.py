import pygame
import Mapa_Zelda

class Link(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("Link 2.2.png")
        self.rect = self.image.get_rect(topleft = pos)

        self.direccion = pygame.math.Vector2()
        self.velocidad = 5


    def teclado(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direccion.y = -1

        elif keys[pygame.K_DOWN]:
            self.direccion.y = 1

        else:
            self.direccion.y = 0

        if keys[pygame.K_RIGHT]:
            self.direccion.x = 1

        elif keys[pygame.K_LEFT]:
            self.direccion.x = -1

        else:
            self.direccion.x = 0

    def mover(self, velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()

        self.rect.center += self.direccion * velocidad

    def update(self):
        self.teclado()
        self.mover(self.velocidad)
