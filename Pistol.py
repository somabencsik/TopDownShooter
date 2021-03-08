import math
import Bullet as b
import pygame

pygame.init()


class Pistol:
    def __init__(self, x=None, y=None, player=None):
        self.x = x
        self.y = y
        self.shootCountdown = 0
        self.owner = player
        self.pistolString = pygame.image.tostring(pygame.image.load("Pistol.png"), "RGB")
        self.bulletSpeed = 10
        self.bullets = []

    def render(self, screen):
        if not self.owner:
            pistolImage = pygame.image.fromstring(self.pistolString, (40, 15), "RGB").convert_alpha()
            screen.blit(pistolImage, (self.x, self.y))
        else:
            pistolImage = pygame.image.fromstring(self.pistolString, (40, 15), "RGB").convert_alpha()
            self.x = self.owner.x + 25
            self.y = self.owner.y + 25
            pistolPos = (self.x, self.y)
            pistolRect = pistolImage.get_rect(center=pistolPos)
            pistolRect[0] += 20

            mx, my = pygame.mouse.get_pos()
            dx, dy = mx - pistolRect.centerx, my - pistolRect.centery
            angle = math.degrees(math.atan2(-dy, dx))

            rot_image = pygame.transform.rotate(pistolImage, angle)
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
