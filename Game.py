import Window as w
import Player as p
import pygame
pygame.init()


class Game:
    def __init__(self):
        self.window = w.Window(1280, 720)
        self.running = True
        self.player = p.Player(50, 50, 50, 50, (255, 200, 69))
        self.bullets = []

    def run(self):
        while self.running:
            self.window.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                keys = pygame.key.get_pressed()

                self.player.movement(keys)

            if pygame.mouse.get_pressed(3)[0]:
                if self.player.currentWeapon:
                    self.player.currentWeapon.shoot(self.bullets)

            self.window.screen.fill((255, 255, 255))

            self.update()
            self.render(self.window.screen)

            pygame.display.update()

        # After closing game
        pygame.quit()

    def render(self, screen):
        self.player.render(screen)
        for bullet in self.bullets:
            bullet.render(screen)

    def update(self):
        self.player.update()
        for bullet in self.bullets:
            bullet.update()
