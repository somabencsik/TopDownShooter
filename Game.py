import Window as w
import GameManager as gm
import NetworkManager as nm
import pygame
pygame.init()


class Game:
    def __init__(self):
        self.window = w.Window(1280, 720)
        self.running = True

        self.network = nm.Network()
        self.player = self.network.getP()

        self.players = []
        self.weapons = []

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
                    self.player.currentWeapon.shoot()

            self.window.screen.fill((255, 255, 255))

            self.update()
            self.render(self.window.screen)

            pygame.display.update()

        # After closing game
        pygame.quit()

    def render(self, screen):
        self.player.render(screen)

        for player in self.players:
            player.render(screen)

    def update(self):
        self.players = self.network.send(self.player)

        self.player.update()
        for player in self.players:
            player.update()
