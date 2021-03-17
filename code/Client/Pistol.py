import math
from code.Client import Bullet as b
import pygame
import os

pygame.init()


class Pistol:
    def __init__(self, x=None, y=None, player=None):
        self.x = x
        self.y = y
        self.shootCountdown = 0
        self.owner = player
        image = os.path.join("C:\\Users\\somabencsik\\Documents\\python\\TopDownShooter\\Assets\\Images\\Pistol.png")
        self.pistolImage = pygame.image.tostring(pygame.image.load(image), "RGBA")
        self.width = 40
        self.height = 15
        self.angle = 0.0
        self.damage = 20
        self.bulletSpeed = 10
        self.bullets = []
        self.allowRotation = True

    def render(self, screen):
        if not self.owner:
            pistolImage = pygame.image.fromstring(self.pistolImage, (self.width, self.height), "RGBA")
            screen.blit(pistolImage, (self.x, self.y))
        else:
            self.x = self.owner.x + 25
            self.y = self.owner.y + 25

            if self.allowRotation:
                pistolImage, pistolImageRect = self.rotate()
                screen.blit(pistolImage, pistolImageRect.topleft)
            else:
                pistolImage = pygame.image.fromstring(self.pistolImage, (self.width, self.height), "RGBA")

                pistolPos = (self.x, self.y)
                pistolRect = pistolImage.get_rect(center=pistolPos)
                pistolRect[0] += 20

                rot_image = pygame.transform.rotate(pistolImage, self.angle)
                rot_image_rect = rot_image.get_rect(center=pistolRect.center)

                screen.blit(rot_image, rot_image_rect.topleft)

        for bullet in self.bullets:
            bullet.render(screen)

    def update(self):
        if self.shootCountdown:
            self.shootCountdown -= 1

        for bullet in self.bullets:
            if bullet.x + bullet.rad / 2 < 0 \
                    or bullet.x - bullet.rad / 2 > pygame.display.get_surface().get_width() \
                    or bullet.y + bullet.rad / 2 < 0 \
                    or bullet.y - bullet.rad / 2 > pygame.display.get_surface().get_height():
                self.bullets.remove(bullet)

            bullet.update()

    def shoot(self):
        if not self.shootCountdown:
            self.bullets.append(b.Bullet(self.x + 20,
                                         self.y,
                                         self.bulletSpeed,
                                         (0, 0, 0), pygame.mouse.get_pos(), 10)
                                )
            self.shootCountdown = 30

    def rotate(self):
        pistolImage = pygame.image.fromstring(self.pistolImage, (self.width, self.height), "RGBA")

        pistolPos = (self.x, self.y)
        pistolRect = pistolImage.get_rect(center=pistolPos)
        pistolRect[0] += 20

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - pistolRect.centerx, my - pistolRect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        self.angle = angle

        rot_image = pygame.transform.rotate(pistolImage, angle)
        rot_image_rect = rot_image.get_rect(center=pistolRect.center)

        return rot_image, rot_image_rect
