import Pistol as p
import pygame
pygame.init()


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.xChange = 0
        self.yChange = 0
        self.currentWeapon = None
            #p.Pistol(player=self)  # TODO: Weapon handling, weapon change

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.currentWeapon:
            self.currentWeapon.render(screen)

    def update(self):
        self.x = self.x + self.xChange
        self.y = self.y + self.yChange
        if self.currentWeapon:
            self.currentWeapon.update()

    def movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.xChange = -self.speed
        if keys[pygame.K_RIGHT]:
            self.xChange = self.speed
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.xChange = 0
        if keys[pygame.K_UP]:
            self.yChange = -self.speed
        if keys[pygame.K_DOWN]:
            self.yChange = self.speed
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            self.yChange = 0
