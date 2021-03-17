import math
import pygame
pygame.init()


class Bullet:
    def __init__(self, x, y, rad, color, destination, speed):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.change = ["x", "y"]
        self.angle = math.atan2(destination[1] - self.y, destination[0] - self.x)
        self.change[0] = math.cos(self.angle) * speed
        self.change[1] = math.sin(self.angle) * speed

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad, 0)

    def update(self):
        self.x = self.x + self.change[0]
        self.y = self.y + self.change[1]
