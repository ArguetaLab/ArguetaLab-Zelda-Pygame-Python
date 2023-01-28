import pygame
import Mapa_Zelda

class Link(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        self.image = pygame.image.load("Link 2.2.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -30)

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

        self.hitbox.x += self.direccion.x * velocidad
        self.coliciones("horizontal")

        self.hitbox.y += self.direccion.y * velocidad
        self.coliciones("vertical")
        self.rect.center = self.hitbox.center

    def coliciones(self, direccion):
        if direccion == "horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.x > 0:
                        self.hitbox.right = sprite.rect.left

                    if self.direccion.x < 0:
                        self.hitbox.left = sprite.rect.right

        if direccion == "vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.y > 0:
                        self.hitbox.bottom = sprite.rect.top

                    if self.direccion.y < 0:
                        self.hitbox.top = sprite.rect.bottom

    def update(self):
        self.teclado()
        self.mover(self.velocidad)
