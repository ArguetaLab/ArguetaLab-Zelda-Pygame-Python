import pygame
import Mapa_Zelda

class Link(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        self.image = pygame.image.load("Link 2.2.png")
        self.rect = self.image.get_rect(topleft = pos)

        self.direccion = pygame.math.Vector2()
        self.velocidad = 5

        self.Obstaculos = obstaculos


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

        self.rect.x += self.direccion.x * velocidad
        self.coliciones("horizontal")

        self.rect.y += self.direccion.y * velocidad
        self.coliciones("vertical")

    def coliciones(self, direccion):
        if direccion == "horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direccion.x > 0:
                        self.rect.right = sprite.rect.left

                    if self.direccion.x < 0:
                        self.rect.left = sprite.rect.right

        if direccion == "vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direccion.y > 0:
                        self.rect.bottom = sprite.rect.top

                    if self.direccion.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.teclado()
        self.mover(self.velocidad)
