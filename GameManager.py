class GameManager:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def checkCollision(self):
        # TODO: Player - Weapon
        # TODO: Enemy - Bullet

        for enemy in self.enemies:
            if enemy == self.player:
                continue

            if enemy.currentWeapon:
                for bullet in enemy.currentWeapon.bullets[:]:
                    hit = self.playerBulletIntersection(bullet)
                    if hit:
                        self.player.hit(20)
                        enemy.currentWeapon.bullets.remove(bullet)

    def playerBulletIntersection(self, bullet):
        bulletCenter = (bullet.x + bullet.rad / 2, bullet.y + bullet.rad / 2)
        bulletDistanceX = abs(bulletCenter[0] - self.player.rect.centerx)
        bulletDistanceY = abs(bulletCenter[1] - self.player.rect.centery)
        if bulletDistanceX > self.player.rect.width / 2.0 + bullet.rad \
                or bulletDistanceY > self.player.rect.height / 2.0 + bullet.rad:
            return False
        if bulletDistanceX <= self.player.rect.width / 2.0 \
                or bulletDistanceY <= self.player.rect.height / 2.0:
            return True
        cornerX = bulletDistanceX - self.player.rect.width / 2.0
        cornerY = bulletDistanceY - self.player.rect.height / 2.0
        cornerDistanceSquare = cornerX ** 2.0 + cornerY ** 2.0
        return cornerDistanceSquare <= bullet.rad ** 2.0
