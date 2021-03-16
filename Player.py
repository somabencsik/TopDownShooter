import Pistol as p
import random as r
import pygame
pygame.init()


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = 100
        self.speed = 5
        self.xChange = 0
        self.yChange = 0
        self.currentWeapon = p.Pistol(player=self)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.respawnTime = 0
        self.checkForDeath = True
        self.alive = True

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def render(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
            if self.currentWeapon:
                self.currentWeapon.render(screen)
        if self.checkForDeath:
            if not self.alive:
                text, textRect = self.makeRespawnText()
                screen.blit(text, textRect)

    def update(self):
        if self.respawnTime > 0 and not self.alive:
            self.respawnTime = self.respawnTime - 1
        else:
            self.x = self.x + self.xChange
            self.y = self.y + self.yChange
            if self.currentWeapon:
                self.currentWeapon.update()

        if self.checkForDeath:
            self.checkDeath()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def checkDeath(self):
        if self.health == 0 and self.alive:
            self.respawnTime = 300
            self.alive = False
            self.width = 0
            self.height = 0
        if self.respawnTime == 0 and not self.alive:
            self.alive = True
            self.x = r.randint(0, 1230)
            self.y = r.randint(0, 670)
            self.width = 50
            self.height = 50
            self.health = 100

    def makeRespawnText(self):
        font = pygame.font.SysFont('arial', 32)
        text = font.render("Respawn in " + str(int(self.respawnTime / 60)), True, (200, 0, 0))
        textRect = text.get_rect()
        textRect.center = (pygame.display.get_surface().get_width() // 2,
                           pygame.display.get_surface().get_height() // 2)
        return text, textRect

    # TODO: More detailed hit: Shoot in head, middle, foot
    def hit(self, damage):
        if self.health - damage >= 0:
            self.health -= damage

    def movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.xChange = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.xChange = self.speed
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_a]):
            self.xChange = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.yChange = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.yChange = self.speed
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_w]):
            self.yChange = 0
